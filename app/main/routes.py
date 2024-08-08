from flask import render_template
from app.main import bp


@bp.route('/')
def index():
    print("Index")
    return render_template('index.html')

# Main
@bp.route('/development-objectives')
def development_objectives():
    print("Development Objectives")
    return render_template('/main/development-objectives.html')

@bp.route('/initiatives')
def initiatives():
    print("Initiatives")
    return render_template('/main/initiatives.html')

@bp.route('/active-initiative-list')
def active_initiative_list():
    print("Active Initiative List")
    return render_template('/main/active-initiative-list.html')

@bp.route('/program-step-initiatives')
def program_step_initiatives():
    print("Program Step Initiatives")
    return render_template('/main/program-step-initiatives.html')

@bp.route('/solution-initiatives')
def solution_initiatives():
    print("Solution Initiatives")
    return render_template('/main/solution-initiatives.html')

@bp.route('/initiative-roadmap')
def initiative_roadmap():
    print("Initiative Roadmap")
    return render_template('/main/initiative-roadmap.html')

@bp.route('/projects')
def projects():
    print("Projects")
    return render_template('/main/projects.html')

#Priority
@bp.route('/priority-matrix')
def priority_matrix():
    print("Priority Matrix")
    return render_template('/priority/priority-matrix.html')

@bp.route('/initiative-priority')
def initiative_priority():
    print("Priority Matrix")
    return render_template('/priority/initiative-priority.html')

#Master Data
@bp.route('/markets-new')
def markets_new():
    print("Markets - New")
    return render_template('/master-data/markets-new.html')

@bp.route('/investment-category')
def investment_category():
    print("Investment Category")
    return render_template('/master-data/investment-category.html')

@bp.route('/program-step')
def program_step():
    print("Program Step")
    return render_template('/master-data/program_step.html')

@bp.route('/theme')
def theme():
    print("Theme")
    return render_template('/master-data/theme.html')

@bp.route('/initiative-states')
def initiative_states():
    print("Initiative States")
    return render_template('/master-data/initiative-states.html')

@bp.route('/product-owners')
def product_owners():
    print("Product Owners")
    return render_template('/master-data/product-owners.html')

@bp.route('/developers')
def developers():
    print("Developers")
    return render_template('/master-data/developers.html')

@bp.route('/developer-skills')
def developer_skills():
    print("Developer Skills")
    return render_template('/master-data/developer-skills.html')

#Other
@bp.route('/configuration')
def configuration():
    print("Configuration")
    return render_template('/other/configuration.html')

@bp.route('/external-pull')
def external_pull():
    print("External Pull")
    return render_template('/other/external-pull.html')

@bp.route('/google')
def google():
    print("Google")
    return render_template('/other/google.html')

@bp.route('/user-management')
def user_management():
    print("User Management")
    return render_template('/other/user-management.html')

@bp.route('/log')
def log():
    print("Log")
    return render_template('/other/log.html')