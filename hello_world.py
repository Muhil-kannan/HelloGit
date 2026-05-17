#!/usr/bin/env python3
"""
A production-ready Hello World script demonstrating best practices in Python,
including type hinting, structured logging, argument parsing, and error handling.
"""

import argparse
import logging
import sys
from typing import List, Optional


def setup_logging(level: int = logging.INFO) -> None:
    """
    Configures the logging system with a standardized format.
    
    Args:
        level: The logging level to use (e.g., logging.INFO).
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
        stream=sys.stdout,
    )


def get_greeting(name: str) -> str:
    """
    Constructs a greeting message.

    Args:
        name: The name of the entity to greet.

    Returns:
        A formatted greeting string.

    Raises:
        ValueError: If the name provided is empty or contains only whitespace.
    """
    if not name or not name.strip():
        raise ValueError("The 'name' parameter must be a non-empty string.")
    
    return f"Hello, {name.strip()}!"


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the script.

    Args:
        argv: Command line arguments. If None, sys.argv is used.

    Returns:
        Exit code: 0 for success, 1 for expected errors, 2 for unexpected failures.
    """
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description="A robust Hello World script following industry standards."
    )
    parser.add_argument(
        "--name",
        type=str,
        default="World",
        help="The name of the person or entity to greet (default: World)."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug-level logging output."
    )

    try:
        args = parser.parse_args(argv)
        
        if args.verbose:
            logging.getLogger().setLevel(logging.DEBUG)
            logger.debug("Verbose logging enabled.")

        greeting_message = get_greeting(args.name)
        
        # In a production environment, we use logging over print to allow 
        # for better log management, redirection, and severity levels.
        logger.info(greeting_message)
        
        return 0

    except ValueError as ve:
        logger.error("Validation failed: %s", ve)
        return 1
    except KeyboardInterrupt:
        logger.warning("Execution interrupted by user.")
        return 130
    except Exception as e:
        # Catch-all for unexpected runtime errors to ensure they are logged
        logger.critical("An unexpected error occurred: %s", e, exc_info=True)
        return 2


if __name__ == "__main__":
    # sys.exit ensures the process returns the correct status code to the shell
    sys.exit(main())