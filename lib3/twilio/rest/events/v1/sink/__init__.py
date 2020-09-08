# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.events.v1.sink.sink_test import SinkTestList
from twilio.rest.events.v1.sink.sink_validate import SinkValidateList


class SinkList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the SinkList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.events.v1.sink.SinkList
        :rtype: twilio.rest.events.v1.sink.SinkList
        """
        super(SinkList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Sinks'.format(**self._solution)

    def create(self, description, sink_configuration, sink_type):
        """
        Create the SinkInstance

        :param unicode description: Sink Description
        :param dict sink_configuration: JSON Sink configuration.
        :param SinkInstance.SinkType sink_type: Sink type.

        :returns: The created SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        data = values.of({
            'Description': description,
            'SinkConfiguration': serialize.object(sink_configuration),
            'SinkType': sink_type,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return SinkInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams SinkInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.sink.SinkInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SinkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.sink.SinkInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SinkInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return SinkPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SinkInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SinkPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SinkContext

        :param sid: A string that uniquely identifies this Sink.

        :returns: twilio.rest.events.v1.sink.SinkContext
        :rtype: twilio.rest.events.v1.sink.SinkContext
        """
        return SinkContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a SinkContext

        :param sid: A string that uniquely identifies this Sink.

        :returns: twilio.rest.events.v1.sink.SinkContext
        :rtype: twilio.rest.events.v1.sink.SinkContext
        """
        return SinkContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.SinkList>'


class SinkPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the SinkPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.events.v1.sink.SinkPage
        :rtype: twilio.rest.events.v1.sink.SinkPage
        """
        super(SinkPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SinkInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.events.v1.sink.SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        return SinkInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.SinkPage>'


class SinkContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the SinkContext

        :param Version version: Version that contains the resource
        :param sid: A string that uniquely identifies this Sink.

        :returns: twilio.rest.events.v1.sink.SinkContext
        :rtype: twilio.rest.events.v1.sink.SinkContext
        """
        super(SinkContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Sinks/{sid}'.format(**self._solution)

        # Dependents
        self._sink_test = None
        self._sink_validate = None

    def fetch(self):
        """
        Fetch the SinkInstance

        :returns: The fetched SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SinkInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the SinkInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    @property
    def sink_test(self):
        """
        Access the sink_test

        :returns: twilio.rest.events.v1.sink.sink_test.SinkTestList
        :rtype: twilio.rest.events.v1.sink.sink_test.SinkTestList
        """
        if self._sink_test is None:
            self._sink_test = SinkTestList(self._version, sid=self._solution['sid'], )
        return self._sink_test

    @property
    def sink_validate(self):
        """
        Access the sink_validate

        :returns: twilio.rest.events.v1.sink.sink_validate.SinkValidateList
        :rtype: twilio.rest.events.v1.sink.sink_validate.SinkValidateList
        """
        if self._sink_validate is None:
            self._sink_validate = SinkValidateList(self._version, sid=self._solution['sid'], )
        return self._sink_validate

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SinkContext {}>'.format(context)


class SinkInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Status(object):
        INITIALIZED = "initialized"
        VALIDATING = "validating"
        ACTIVE = "active"
        FAILED = "failed"

    class SinkType(object):
        KINESIS = "kinesis"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the SinkInstance

        :returns: twilio.rest.events.v1.sink.SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        super(SinkInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'description': payload.get('description'),
            'sid': payload.get('sid'),
            'sink_configuration': payload.get('sink_configuration'),
            'sink_type': payload.get('sink_type'),
            'status': payload.get('status'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SinkContext for this SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkContext
        """
        if self._context is None:
            self._context = SinkContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def date_created(self):
        """
        :returns: The date this Sink was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Sink was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def description(self):
        """
        :returns: Sink Description
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Sink.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def sink_configuration(self):
        """
        :returns: JSON Sink configuration.
        :rtype: dict
        """
        return self._properties['sink_configuration']

    @property
    def sink_type(self):
        """
        :returns: Sink type.
        :rtype: SinkInstance.SinkType
        """
        return self._properties['sink_type']

    @property
    def status(self):
        """
        :returns: The Status of this Sink
        :rtype: SinkInstance.Status
        """
        return self._properties['status']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: Nested resource URLs.
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the SinkInstance

        :returns: The fetched SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SinkInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def sink_test(self):
        """
        Access the sink_test

        :returns: twilio.rest.events.v1.sink.sink_test.SinkTestList
        :rtype: twilio.rest.events.v1.sink.sink_test.SinkTestList
        """
        return self._proxy.sink_test

    @property
    def sink_validate(self):
        """
        Access the sink_validate

        :returns: twilio.rest.events.v1.sink.sink_validate.SinkValidateList
        :rtype: twilio.rest.events.v1.sink.sink_validate.SinkValidateList
        """
        return self._proxy.sink_validate

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SinkInstance {}>'.format(context)
