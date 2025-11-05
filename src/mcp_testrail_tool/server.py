import os
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

load_dotenv()
mcp = FastMCP("testrail")

BASE_URL = os.getenv("TESTRAIL_URL")
AUTH = (os.getenv("TESTRAIL_USER"), os.getenv("TESTRAIL_API_KEY"))

def testrail_get(endpoint: str):
    url = f"{BASE_URL}/index.php?/api/v2/{endpoint}"
    try:
        response = requests.get(url, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"API error on {endpoint}: {str(e)}"))

def status_label_map(status_id: int) -> str:
    return {
        1: "Passed", 2: "Blocked", 3: "Untested", 4: "Retest", 5: "Failed", 6: "N/A"
    }.get(status_id, f"Status {status_id}")

@mcp.tool()
def get_projects() -> list:
    return testrail_get("get_projects")

@mcp.tool()
def get_test_runs(project_id: int) -> dict:
    response = testrail_get(f"get_runs/{project_id}&limit=250")
    if not isinstance(response, dict) or "runs" not in response:
        raise McpError(ErrorData(INTERNAL_ERROR, "Expected a dictionary with 'runs' key."))

    safe_trim = [
        {
            "id": r.get("id"),
            "name": r.get("name", ""),
            "url": f"{BASE_URL}/index.php?/runs/view/{r.get('id')}"
        }
        for r in response["runs"] if isinstance(r, dict)
    ]

    return {
        "offset": response.get("offset", 0),
        "limit": response.get("limit", 250),
        "size": response.get("size", len(safe_trim)),
        "_links": response.get("_links", {}),
        "runs": safe_trim
    }

@mcp.tool()
def get_test_runs_page(project_id: int, offset: int = 250) -> dict:
    limit = 250
    response = testrail_get(f"get_runs/{project_id}&limit={limit}&offset={offset}")
    if not isinstance(response, dict) or "runs" not in response:
        raise McpError(ErrorData(INTERNAL_ERROR, "Expected a dictionary with 'runs' key."))

    page_runs = [
        {
            "id": r.get("id"),
            "name": r.get("name", ""),
            "url": f"{BASE_URL}/index.php?/runs/view/{r.get('id')}"
        }
        for r in response["runs"] if isinstance(r, dict)
    ]

    return {
        "offset": response.get("offset", offset),
        "limit": limit,
        "size": len(page_runs),
        "runs": page_runs
    }

@mcp.tool()
def get_test_run(run_id: int) -> dict:
    return testrail_get(f"get_run/{run_id}")

@mcp.tool()
def get_test(test_id: int) -> dict:
    test = testrail_get(f"get_test/{test_id}")
    return {
        "test_id": test.get("id"),
        "case_id": test.get("case_id"),
        "status_id": test.get("status_id"),
        "status_label": status_label_map(test.get("status_id")),
        "title": test.get("title", ""),
        "url": f"{BASE_URL}/index.php?/tests/view/{test_id}"
    }

@mcp.tool()
def get_final_statuses_for_run(run_id: int, status_ids: list[int]) -> dict:
    results_response = testrail_get(f"get_results_for_run/{run_id}")
    test_ids = {r["test_id"] for r in results_response.get("results", []) if "test_id" in r}

    latest_result_map = {}
    for r in results_response.get("results", []):
        test_id = r.get("test_id")
        if test_id and test_id not in latest_result_map:
            latest_result_map[test_id] = r

    merged = []
    for test_id in test_ids:
        test = testrail_get(f"get_test/{test_id}")
        if test.get("status_id") in status_ids:
            result = latest_result_map.get(test_id, {})
            merged.append({
                "test_id": test.get("id"),
                "case_id": test.get("case_id"),
                "status_id": test.get("status_id"),
                "status_label": status_label_map(test.get("status_id")),
                "title": test.get("title", ""),
                "comment": result.get("comment", ""),
                "defects": result.get("defects", ""),
                "elapsed": result.get("elapsed", ""),
                "url": f"{BASE_URL}/index.php?/tests/view/{test_id}"
            })

    return {
        "run_id": run_id,
        "status_ids": status_ids,
        "count": len(merged),
        "results": merged
    }
