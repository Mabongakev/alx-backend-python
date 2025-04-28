#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Get a random float between 0 and max_delay"""
    delay = random.uniform(0, max_delay) 
    """Generate a random delay.""" 
    await asyncio.sleep(delay)   
     """return the delay"""
    return delay   
