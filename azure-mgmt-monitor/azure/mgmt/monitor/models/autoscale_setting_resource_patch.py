# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AutoscaleSettingResourcePatch(Model):
    """The autoscale setting object for patch operations.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param profiles: the collection of automatic scaling profiles that specify
     different scaling parameters for different time periods. A maximum of 20
     profiles can be specified.
    :type profiles: list[~azure.mgmt.monitor.models.AutoscaleProfile]
    :param notifications: the collection of notifications.
    :type notifications:
     list[~azure.mgmt.monitor.models.AutoscaleNotification]
    :param enabled: the enabled flag. Specifies whether automatic scaling is
     enabled for the resource. The default value is 'true'. Default value: True
     .
    :type enabled: bool
    :param name: the name of the autoscale setting.
    :type name: str
    :param target_resource_uri: the resource identifier of the resource that
     the autoscale setting should be added to.
    :type target_resource_uri: str
    """

    _validation = {
        'profiles': {'required': True, 'max_items': 20},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'profiles': {'key': 'properties.profiles', 'type': '[AutoscaleProfile]'},
        'notifications': {'key': 'properties.notifications', 'type': '[AutoscaleNotification]'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'name': {'key': 'properties.name', 'type': 'str'},
        'target_resource_uri': {'key': 'properties.targetResourceUri', 'type': 'str'},
    }

    def __init__(self, profiles, tags=None, notifications=None, enabled=True, name=None, target_resource_uri=None):
        self.tags = tags
        self.profiles = profiles
        self.notifications = notifications
        self.enabled = enabled
        self.name = name
        self.target_resource_uri = target_resource_uri
