"""Base agent class for all specialized agents"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
import logging

from src.core.knowledge_base import KnowledgeBase

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Base class for all agents"""
    
    def __init__(self, knowledge_base: KnowledgeBase, name: str):
        self.knowledge_base = knowledge_base
        self.name = name
        self.logger = logging.getLogger(f"Agent:{name}")
    
    @abstractmethod
    async def execute(self, *args, **kwargs) -> Dict[str, Any]:
        """Execute agent's main task"""
        pass
    
    def log_action(self, action: str, details: Optional[Dict] = None):
        """Log agent action"""
        message = f"[{self.name}] {action}"
        if details:
            message += f" - {details}"
        self.logger.info(message)
