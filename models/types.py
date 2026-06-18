from typing import Literal


AgentRank = Literal['Junior', 'Senior', 'Commander']


MissionStatus = Literal['NEW', 'ASSIGNED',
                        'IN_PROGRESS', 'COMPLETED',
                        'FAILED', 'CANCELLED']


MissionRiskLevel = Literal['LOW', 'MEDIUM',
                        'HIGH', 'CRITICAL']