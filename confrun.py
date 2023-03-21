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
    return "http://quick.testpub.cn"


def title():
    """
    setting report title
    """
    return "Quick接口自动化平台"


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
