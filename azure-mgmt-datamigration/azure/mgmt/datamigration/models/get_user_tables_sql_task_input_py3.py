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


class GetUserTablesSqlTaskInput(Model):
    """Input for the task that collects user tables for the given list of
    databases.

    All required parameters must be populated in order to send to Azure.

    :param connection_info: Required. Connection information for SQL Server
    :type connection_info: ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param selected_databases: Required. List of database names to collect
     tables for
    :type selected_databases: list[str]
    """

    _validation = {
        'connection_info': {'required': True},
        'selected_databases': {'required': True},
    }

    _attribute_map = {
        'connection_info': {'key': 'connectionInfo', 'type': 'SqlConnectionInfo'},
        'selected_databases': {'key': 'selectedDatabases', 'type': '[str]'},
    }

    def __init__(self, *, connection_info, selected_databases, **kwargs) -> None:
        super(GetUserTablesSqlTaskInput, self).__init__(**kwargs)
        self.connection_info = connection_info
        self.selected_databases = selected_databases
