import os

import newrelic.agent
from datadog import initialize, statsd

initialize(**{"statsd_host": "192.168.200.250", "statsd_port": 8125})

JOBS_MELI_NOTIFICATIONS_CREATED = "jobs.meli.notifications.created"
JOBS_MELI_NOTIFICATIONS_UPDATED = "jobs.meli.notifications.updated"
TASKS_CLEAN_FRAME_WITHOUT_INFO = "tasks.clean_frame_without_info"
TASKS_CREATE_FRAME_POOL_PROCESSING = "tasks.create_frame_pool_processing"
TASKS_PROCESS_EACH_FRAME = "tasks.process_each_frame"
TASKS_PROCESS_EACH_FRAME_NO_INFO = "tasks.process_each_frame.no_info"
TASKS_SPLIT_VIDEO_IN_FRAMES_FRAMES = "tasks.split_video_in_frames.frames"
TASKS_SYNC_PRODUCT_VARIATION = "tasks.sync_product_variation"
TASKS_VIDEO_PROCESSING_STATUS = "tasks.video_processing_status"
TASKS_CORE_REQUESTS = "tasks.core.requests"
TASKS_CORE_COUNT_REQUESTS = "tasks.core.count.requests"


def _process_tags(tags):
    """
    Format a dict with tags to the format expected by datadogpy.
    For example:
    {
        "foo": "bar",
        "baz": "quux"
    }
    Translates to: ["foo:bar", "baz:quux"]
    Args:
        tags (dict or None): a dictionary of "tag name": "tag value" items, or None.
    Returns:
        list: tags as expected by datadogpy.
    """
    base_tags = {"scope": os.getenv("SCOPE", "production")}

    _tags = tags or {}
    _tags.update(base_tags)
    return ["{}:{}".format(tag, value) for tag, value in _tags.items()]


def record_count(name, increment=1, tags=None):
    """
    Counters track how many times something happens per second.
    Implemented as Datadog Counter (https://docs.datadoghq.com/developers/metrics/counts/).
    Args:
        name (str): metric name.
        increment (int, optional): The counter is incremented by this given value.
            Defaults to 1.
        tags (dict, optional): Dictionary of "tag name": "tag value" items.
            Defaults to None.
    """
    name = f"af.{name}"
    statsd.increment(name, increment, tags=_process_tags(tags))


def record_gauge(name, value, tags=None):
    """
    Gauges measure the value of a particular thing over time.
    They are implemented as [Datadog Gauges](https://docs.datadoghq.com/developers/metrics/gauges/)
    Args:
        name (str): metric name.
        value (number): value to record for the flush interval.
        tags (dict, optional): Dictionary of "tag name": "tag value" items. Defaults to None.
    """
    name = f"af.{name}"
    statsd.gauge(name, value, tags=_process_tags(tags))


def record_histogram(name, value, tags=None):
    """
    Histograms measure the statistical distribution of a set of values.
    They are implemented as Datadog Histograms
    https://docs.datadoghq.com/developers/metrics/histograms/
    For a metric named `my_metric`, the following metrics are generated:
    `my_metric.avg`, `my_metric.count`, `my_metric.median`, `my_metric.95percentile`,
    `my_metric.max` and `my_metric.min`
    Args:
        name (str): metric name.
        value (number): The value to add to the distribution computation.
        tags (dict, optional): Dictionary of "tag name": "tag value" items. Defaults to None.
    """
    name = f"af.{name}"
    statsd.histogram(name, value, tags=_process_tags(tags))


def newrelic_event(event_type, tags):
    _tags = _process_tags(tags)
    newrelic.agent.record_custom_event(event_type, _tags)
