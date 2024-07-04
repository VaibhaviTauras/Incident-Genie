"""Auto migrations

Revision ID: ee1aedd61c4f
Revises: 
Create Date: 2024-06-29 09:16:16.526637

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ee1aedd61c4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organisations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_organisations_id'), 'organisations', ['id'], unique=False)
    op.create_index(op.f('ix_organisations_name'), 'organisations', ['name'], unique=False)
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=320), nullable=True),
    sa.Column('last_name', sa.String(length=320), nullable=True),
    sa.Column('email', sa.String(length=320), nullable=True),
    sa.Column('is_present', sa.Boolean(), server_default='f', nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=True)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=True)
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organisation_id', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('response_type', sa.String(), nullable=True),
    sa.Column('question_type', sa.String(), nullable=True),
    sa.Column('options', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['organisation_id'], ['organisations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questions_id'), 'questions', ['id'], unique=False)
    op.drop_table('client_admin_login_session')
    op.drop_table('project_details')
    op.drop_index('ix_client_role_module_permission_client_module_id', table_name='client_role_module_permission')
    op.drop_index('ix_client_role_module_permission_client_permission_id', table_name='client_role_module_permission')
    op.drop_index('ix_client_role_module_permission_client_role_id', table_name='client_role_module_permission')
    op.drop_table('client_role_module_permission')
    op.drop_index('ix_client_role_subsidiary_master_id', table_name='client_role')
    op.drop_table('client_role')
    op.drop_table('project_details_workflow')
    op.drop_index('ix_client_user_client_role_id', table_name='client_user')
    op.drop_index('ix_client_user_user_master_id', table_name='client_user')
    op.drop_table('client_user')
    op.drop_table('task_type_master')
    op.drop_table('client_permission')
    op.drop_table('severity_master')
    op.drop_table('client_module')
    op.drop_index('ix_offline_chatbot_name_language_language_master_id', table_name='offline_chatbot_name_language')
    op.drop_index('ix_offline_chatbot_name_language_offline_chatbot_master_id', table_name='offline_chatbot_name_language')
    op.drop_table('offline_chatbot_name_language')
    op.drop_table('default_workflow')
    op.drop_index('ix_offline_chatbot_master_chatbot_category_master_id', table_name='offline_chatbot_master')
    op.drop_table('offline_chatbot_master')
    op.drop_index('ix_domain_master_organization_master_id', table_name='domain_master')
    op.drop_constraint('domain_master_organization_master_id_fkey', 'domain_master', type_='foreignkey')
    op.drop_column('domain_master', 'organization_master_id')
    op.add_column('subsidiary_details', sa.Column('contact_person_name', sa.String(length=250), nullable=True))
    op.add_column('subsidiary_details', sa.Column('client_admin_name', sa.String(length=250), nullable=True))
    op.add_column('subsidiary_details', sa.Column('client_admin_email', sa.String(length=320), nullable=True))
    op.add_column('subsidiary_details', sa.Column('client_admin_phone_code', sa.String(length=5), nullable=True))
    op.add_column('subsidiary_details', sa.Column('client_admin_mobile_no', sa.String(length=12), nullable=True))
    op.drop_column('subsidiary_details', 'contact_person_first_name')
    op.drop_column('subsidiary_details', 'contact_person_last_name')
    op.add_column('subsidiary_theme_json', sa.Column('theme_json', sa.JSON(), nullable=True))
    op.drop_index('ix_subsidiary_theme_json_theme_id', table_name='subsidiary_theme_json')
    op.drop_constraint('subsidiary_theme_json_theme_id_fkey', 'subsidiary_theme_json', type_='foreignkey')
    op.drop_column('subsidiary_theme_json', 'theme_id')
    op.drop_column('theme_master', 'theme_json')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('theme_master', sa.Column('theme_json', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('subsidiary_theme_json', sa.Column('theme_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('subsidiary_theme_json_theme_id_fkey', 'subsidiary_theme_json', 'theme_master', ['theme_id'], ['id'])
    op.create_index('ix_subsidiary_theme_json_theme_id', 'subsidiary_theme_json', ['theme_id'], unique=False)
    op.drop_column('subsidiary_theme_json', 'theme_json')
    op.add_column('subsidiary_details', sa.Column('contact_person_last_name', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.add_column('subsidiary_details', sa.Column('contact_person_first_name', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.drop_column('subsidiary_details', 'client_admin_mobile_no')
    op.drop_column('subsidiary_details', 'client_admin_phone_code')
    op.drop_column('subsidiary_details', 'client_admin_email')
    op.drop_column('subsidiary_details', 'client_admin_name')
    op.drop_column('subsidiary_details', 'contact_person_name')
    op.add_column('domain_master', sa.Column('organization_master_id', sa.UUID(), autoincrement=False, nullable=True))
    op.create_foreign_key('domain_master_organization_master_id_fkey', 'domain_master', 'organization_master', ['organization_master_id'], ['id'])
    op.create_index('ix_domain_master_organization_master_id', 'domain_master', ['organization_master_id'], unique=False)
    op.create_table('offline_chatbot_master',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('chatbot_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('chatbot_icon', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('chatbot_category_master_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chatbot_category_master_id'], ['chatbot_category_master.id'], name='offline_chatbot_master_chatbot_category_master_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='offline_chatbot_master_pkey'),
    sa.UniqueConstraint('id', name='offline_chatbot_master_id_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_offline_chatbot_master_chatbot_category_master_id', 'offline_chatbot_master', ['chatbot_category_master_id'], unique=False)
    op.create_table('default_workflow',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('default_workflow_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('TAT_working_days', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('task_type_master_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('severity_master_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['severity_master_id'], ['severity_master.id'], name='default_workflow_severity_master_id_fkey'),
    sa.ForeignKeyConstraint(['task_type_master_id'], ['task_type_master.id'], name='default_workflow_task_type_master_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='default_workflow_pkey'),
    sa.UniqueConstraint('id', name='default_workflow_id_key')
    )
    op.create_table('offline_chatbot_name_language',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('chatbot_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('offline_chatbot_master_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('language_master_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['language_master_id'], ['language_master.id'], name='offline_chatbot_name_language_language_master_id_fkey'),
    sa.ForeignKeyConstraint(['offline_chatbot_master_id'], ['offline_chatbot_master.id'], name='offline_chatbot_name_language_offline_chatbot_master_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='offline_chatbot_name_language_pkey'),
    sa.UniqueConstraint('id', name='offline_chatbot_name_language_id_key')
    )
    op.create_index('ix_offline_chatbot_name_language_offline_chatbot_master_id', 'offline_chatbot_name_language', ['offline_chatbot_master_id'], unique=False)
    op.create_index('ix_offline_chatbot_name_language_language_master_id', 'offline_chatbot_name_language', ['language_master_id'], unique=False)
    op.create_table('client_module',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('client_module_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='client_module_pkey'),
    sa.UniqueConstraint('id', name='client_module_id_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('severity_master',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('severity_master_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='severity_master_pkey'),
    sa.UniqueConstraint('id', name='severity_master_id_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('client_permission',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('client_permission_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='client_permission_pkey'),
    sa.UniqueConstraint('id', name='client_permission_id_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('task_type_master',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('task_type_master_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='task_type_master_pkey'),
    sa.UniqueConstraint('id', name='task_type_master_id_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('client_user',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('user_master_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('phone_code', sa.VARCHAR(length=5), autoincrement=False, nullable=True),
    sa.Column('mobile_no', sa.VARCHAR(length=12), autoincrement=False, nullable=True),
    sa.Column('client_role_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('profile_pic', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('reporting_manager_user_subsidiary_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('job_function', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('business_line', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['client_role_id'], ['client_role.id'], name='client_user_client_role_id_fkey'),
    sa.ForeignKeyConstraint(['reporting_manager_user_subsidiary_id'], ['user_subsidiary.id'], name='client_user_reporting_manager_user_subsidiary_id_fkey'),
    sa.ForeignKeyConstraint(['user_master_id'], ['user_master.id'], name='client_user_user_master_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='client_user_pkey'),
    sa.UniqueConstraint('id', name='client_user_id_key')
    )
    op.create_index('ix_client_user_user_master_id', 'client_user', ['user_master_id'], unique=False)
    op.create_index('ix_client_user_client_role_id', 'client_user', ['client_role_id'], unique=False)
    op.create_table('project_details_workflow',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('project_details_workflow_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('project_details_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('task_type_master_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('severity_master_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('TAT_working_days', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('level1_user_subsidiary_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('level2_user_subsidiary_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('level3_user_subsidiary_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['level1_user_subsidiary_id'], ['user_subsidiary.id'], name='project_details_workflow_level1_user_subsidiary_id_fkey'),
    sa.ForeignKeyConstraint(['level2_user_subsidiary_id'], ['user_subsidiary.id'], name='project_details_workflow_level2_user_subsidiary_id_fkey'),
    sa.ForeignKeyConstraint(['level3_user_subsidiary_id'], ['user_subsidiary.id'], name='project_details_workflow_level3_user_subsidiary_id_fkey'),
    sa.ForeignKeyConstraint(['project_details_id'], ['project_details.id'], name='project_details_workflow_project_details_id_fkey'),
    sa.ForeignKeyConstraint(['severity_master_id'], ['severity_master.id'], name='project_details_workflow_severity_master_id_fkey'),
    sa.ForeignKeyConstraint(['task_type_master_id'], ['task_type_master.id'], name='project_details_workflow_task_type_master_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='project_details_workflow_pkey'),
    sa.UniqueConstraint('id', name='project_details_workflow_id_key')
    )
    op.create_table('client_role',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('client_role_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('subsidiary_master_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['subsidiary_master_id'], ['subsidiary_master.id'], name='client_role_subsidiary_master_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='client_role_pkey'),
    sa.UniqueConstraint('id', name='client_role_id_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_client_role_subsidiary_master_id', 'client_role', ['subsidiary_master_id'], unique=False)
    op.create_table('client_role_module_permission',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('client_role_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('client_module_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('client_permission_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['client_module_id'], ['client_module.id'], name='client_role_module_permission_client_module_id_fkey'),
    sa.ForeignKeyConstraint(['client_permission_id'], ['client_permission.id'], name='client_role_module_permission_client_permission_id_fkey'),
    sa.ForeignKeyConstraint(['client_role_id'], ['client_role.id'], name='client_role_module_permission_client_role_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='client_role_module_permission_pkey'),
    sa.UniqueConstraint('id', name='client_role_module_permission_id_key')
    )
    op.create_index('ix_client_role_module_permission_client_role_id', 'client_role_module_permission', ['client_role_id'], unique=False)
    op.create_index('ix_client_role_module_permission_client_permission_id', 'client_role_module_permission', ['client_permission_id'], unique=False)
    op.create_index('ix_client_role_module_permission_client_module_id', 'client_role_module_permission', ['client_module_id'], unique=False)
    op.create_table('project_details',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('subsidiary_master_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('code', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['subsidiary_master_id'], ['subsidiary_master.id'], name='project_details_subsidiary_master_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='project_details_pkey')
    )
    op.create_table('client_admin_login_session',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('client_admin_user_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('access_token', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('refresh_token', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('at_expiry', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('rt_expiry', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_by', sa.UUID(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='client_admin_login_session_pkey'),
    sa.UniqueConstraint('id', name='client_admin_login_session_id_key')
    )
    op.drop_index(op.f('ix_questions_id'), table_name='questions')
    op.drop_table('questions')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_organisations_name'), table_name='organisations')
    op.drop_index(op.f('ix_organisations_id'), table_name='organisations')
    op.drop_table('organisations')
    # ### end Alembic commands ###
