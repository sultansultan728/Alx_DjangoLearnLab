# Django Permissions & Groups Setup

This module demonstrates how to manage access control using Django groups and custom permissions.

## 1. Custom Permissions (models.py)

The `Article` model includes four custom permissions:

- `can_view` – View article list and details  
- `can_create` – Create new articles  
- `can_edit` – Edit existing articles  
- `can_delete` – Delete articles  

These are defined in the model's Meta class.

## 2. Groups Setup

Three groups are created:

### Viewers
- can_view

### Editors
- can_view  
- can_create  
- can_edit  

### Admins
- can_view  
- can_create  
- can_edit  
- can_delete  

Groups can be created manually in Django Admin or automatically using:


