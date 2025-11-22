#!/usr/bin/env python
"""
Generate a new Django SECRET_KEY for production use.
Run this script and copy the output to your Render environment variables.
"""

from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    secret_key = get_random_secret_key()
    print("\n" + "="*70)
    print("🔑 NEW DJANGO SECRET KEY GENERATED")
    print("="*70)
    print(f"\n{secret_key}\n")
    print("="*70)
    print("⚠️  IMPORTANT: Keep this secret! Add it to Render environment variables.")
    print("="*70 + "\n")
