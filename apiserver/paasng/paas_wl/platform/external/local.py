"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except
in compliance with the License. You may obtain a copy of the License at

    http://opensource.org/licenses/MIT

Unless required by applicable law or agreed to in writing, software distributed under
the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific language governing permissions and
limitations under the License.

We undertake not to change the open source license (MIT license) applicable
to the current version of the project delivered to anyone in the future.
"""
from typing import Dict, Optional

from paasng.engine.constants import JobStatus
from paasng.engine.deploy.steps.release import ApplicationReleaseMgr
from paasng.engine.models import Deployment
from paasng.engine.models.offline import OfflineOperation
from paasng.platform.applications.models import ModuleEnvironment
from paasng.platform.applications.signals import module_environment_offline_success
from paasng.platform.operations.models import Operation


class LocalPlatformSvcClient:
    """Client for "apiserver" module, uses local module"""

    def finish_release(self, deployment_id: str, status: str, error_detail: str):
        mgr = ApplicationReleaseMgr.from_deployment_id(deployment_id)
        mgr.callback_release(JobStatus(status), error_detail)

    def finish_archive(self, operation_id: str, status: str, error_detail: str):
        offline_op = OfflineOperation.objects.get(id=operation_id)
        if status == JobStatus.SUCCESSFUL:
            offline_op.set_successful()
        else:
            offline_op.set_failed(error_detail)

        module_environment_offline_success.send(
            sender=OfflineOperation, offline_instance=offline_op, environment=offline_op.app_environment.environment
        )

    def retrieve_deployment(self, deployment_id: str) -> Deployment:
        return Deployment.objects.get(pk=deployment_id)

    def create_operation_log(
        self,
        env: ModuleEnvironment,
        operate_type: int,
        operator: str,
        extra_values: Optional[Dict] = None,
    ):
        """Create an operation log for application

        :returns: None if creation succeeded
        :raises: PlatClientRequestError
        """
        Operation.objects.create(
            application=env.application,
            type=operate_type,
            user=operator,
            region=env.application.region,
            module_name=env.module.name,
            source_object_id=str(env.id),
            extra_values=extra_values,
        )
