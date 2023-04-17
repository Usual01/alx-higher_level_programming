#!/usr/bin/python3
def magic_string():
    m_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool" for i in range(m_string.count)])
