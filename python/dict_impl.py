#!/bin/env python3
import inspect
import numpy as np
from base52_number import base52_number
# This is going to be a custom dictionary implementation


def prod_mod_hash_func(num_slots: int, s: str) -> int:
    product = np.product([ord(char) for char in s])
    return product % num_slots


def check_func_sig(func, expected_signature):
    signature = inspect.signature(func)
    if expected_signature == f"{signature}":
        return True
    return False


class HashTable:
    def __init__(self, num_slots: int, hash_func: object,
                 resizable: bool = False):
        self.__check_args(hash_func)
        self.__hash_func = hash_func
        # [[('key', 'val'), ... ], ... ]
        self.__buckets = [[] for _ in range(num_slots)]
        self.__num_slots = num_slots

    def __check_args(self, hash_func):
        hash_func_sig = "(num_slots: int, s: str) -> int"

        if not callable(hash_func) or not check_func_sig(hash_func,
                                                         hash_func_sig):
            raise ValueError(
                f"hash_func must have signature:\n'{hash_func_sig}' "
                f"not:\n'{inspect.signature(hash_func)}'")

    def __repr__(self):
        rows = [f"b{ii}: {arr}" for ii, arr in enumerate(self.__buckets)]
        return '\n'.join(rows)

    def get(self, key):
        key_hash = self.__hash_func(self.__num_slots, key)
        bucket = self.__buckets[key_hash]

        if len(bucket) >= 1:
            for k, v in bucket:
                if k == key:
                    return v
        raise KeyError(f"Key '{key}' is not set")

    def set(self, key, val):
        key_hash = self.__hash_func(self.__num_slots, key)
        bucket = self.__buckets[key_hash]
        entry_tup = (key, val)
        for ii, k_v in enumerate(bucket):
            if k_v[0] == key:
                self.__buckets[key_hash][ii] = entry_tup
                return
        self.__buckets[key_hash].append(entry_tup)


foo = HashTable(10, prod_mod_hash_func)

foo.set("a", 7)
print(foo)

#

