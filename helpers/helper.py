function processData(data) {
    if (!data) {
        return null;
    }
    return data.map(item => ({
        id: item.id,
        name: item.name,
        processed: true
    }));
}

module.exports = { processData };


"""
Probable Adventure - Performance Improvement
"""

import logging
from functools import lru_cache

logger = logging.getLogger(__name__)

@lru_cache(maxsize=128)
def cached_computation(value):
    """Cached computation for better performance"""
    logger.debug(f"Computing value: {value}")
    # Complex computation here
    return value ** 2

def batch_process(items, batch_size=100):
    """Process items in batches for better memory usage"""
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        yield process_batch(batch)

def process_batch(batch):
    """Process a single batch"""
    return [item.upper() for item in batch]
