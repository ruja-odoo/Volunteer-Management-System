{
    "name": "Volunteer Management",
    "version": "1.0",
    "summary": "A module for managing volunteers.",
    "description": """
        The Volunteer Management System module in Odoo is a comprehensive solution designed to 
        streamline the recruitment, scheduling, and tracking of volunteers for various events, 
        activities, and projects within organizations. It facilitates volunteer registration, 
        opportunity management, assignment scheduling, skill matching, availability tracking, 
        event coordination, communication, feedback collection, and evaluation.
        This module is developed by ruja-odoo.
    """,
    "author": "ruja-odoo",
    "category": "Volunteer",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/volunteer_skills_views.xml",
        "views/volunteer_views.xml",
        "views/volunteer_event.xml",
        "views/volunteer_menus.xml",
    ],
    "demo": [
        # Add demo data files if needed
        # Example: 'demo/estate_demo.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
