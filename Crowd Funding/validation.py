#! /bin/python3

import re as regex

def validate_name (name):
    pattern = r'^[A-Za-z\ ]+$'
    return bool(regex.fullmatch(pattern, name))

def validate_email (email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(regex.fullmatch(pattern, email))

def validate_password (password):
    return len(password) > 8

def validate_mobile (mobile):
    pattern = r'^(010|012|011|015)[0-9]{8}$'
    return bool(regex.fullmatch(pattern, mobile))

def validate_user (first_name, last_name, email, password, mobile):
    validation_result = [
        validate_name(first_name),
        validate_name(last_name),
        validate_email(email),
        validate_password(password),
        validate_mobile(mobile),
    ]
    
    return all(validation_result)

def validate_target (target):
    return target.isdigit() and int(target) >= 0

def validate_date (date):
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    return bool(regex.fullmatch(pattern, date))

def validate_project (title, target, start_date, end_date):
    validation_result = [
        validate_name(title),
        validate_target(target),
        validate_date(start_date),
        validate_date(end_date),
    ]
    
    return all(validation_result)