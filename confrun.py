from seldom.utils import cache
from seldom.logging import log

def start_run():
    """
    Test the hook function before running
    """
    log.info("running test before")
    cache.clear()

def end_run():
    """
    Test the hook function after running
    """
    log.info("running test after")


def base_url():
    """
    http test
    api base url
    """
    return "https://httpbin.org"


def title():
    """
    setting report title
    """
    return "seldom接口自动化测试演示用例"


def tester():
    """
    setting report tester
    """
    return "虫师"


def description():
    """
    setting report description
    """
    return ["windows 11"]


def debug():
    """
    debug mod
    """
    return False


def rerun():
    """
    error/failure rerun times
    """
    return 2
