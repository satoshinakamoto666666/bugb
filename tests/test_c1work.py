from c1work import run_c1work


def test_run_c1work_default_and_custom():
    res = run_c1work()
    assert res.task_id == "c1work"
    assert res.account == "p account"
    assert res.status == "completed"
    assert len(res.digest_sha256) == 64
