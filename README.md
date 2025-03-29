# Task Manager

A simple command-line task management application built with Python and SQLite.

## Overview

This Task Manager allows you to keep track of your tasks with features to add, view, complete, and delete tasks. It's designed to be straightforward yet functional, with a modular architecture that makes it easy to extend.

## Features

- Create tasks
- View all incomplete tasks
- View all tasks
- View detailed information about specific task
- Update task status
- Delete tasks
- Data persistence using SQLite database

## Project Structure

```graphsql
task_manager/
│
├── database.py        # Database operations
├── task_operations.py # Task CRUD operations
├── user_interface.py  # CLI and user interaction
├── task.py            # Task class definition
├── config.py          # Configuration settings
└── main.py            # Entry point
```

## Prerequisites

- Python 3.6 or higher
- No external packages required (uses only standard library)

## Usage

Run the application with:

```bash
python main.py
```
