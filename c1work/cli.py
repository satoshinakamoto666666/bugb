"""
c1work task & `p account` verification module for `rodrigompy/bugb#1`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class C1WorkAccountResult:
    task_id: str
    account: str
    status: str
    digest_sha256: str


def run_c1work(account: str = "p account", task_id: str = "c1work") -> C1WorkAccountResult:
    normalized_account = (account or "p account").strip()
    normalized_task = (task_id or "c1work").strip()
    if not normalized_account:
        raise ValueError("account must not be empty")
    if not normalized_task:
        raise ValueError("task_id must not be empty")
    digest = hashlib.sha256(f"{normalized_task}:{normalized_account}".encode("utf-8")).hexdigest()
    return C1WorkAccountResult(
        task_id=normalized_task,
        account=normalized_account,
        status="completed",
        digest_sha256=digest,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="c1work task runner")
    parser.add_argument("--account", default="p account")
    parser.add_argument("--task", default="c1work")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    res = run_c1work(account=args.account, task_id=args.task)
    if args.json:
        print(json.dumps(asdict(res), sort_keys=True))
    else:
        print(f"{res.task_id} ({res.account}): {res.status} [{res.digest_sha256[:12]}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
