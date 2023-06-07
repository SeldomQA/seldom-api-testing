from seldom.utils import cache


def start_run():
    """
    Test the hook function before running
    """
    cache.clear()


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
