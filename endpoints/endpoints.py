class MILESTONE:
    GET_MILESTONE = "get_milestone"
    GET_MILESTONES = "get_milestones"
    ADD_MILESTONE = "add_milestone"
    UPDATE_MILESTONE = "update_milestone"
    DELETE_MILESTONE = "delete_milestone"


class PLAN:
    GET_PLAN = "get_plan"
    GET_PLANS = "get_plans"
    ADD_PLAN = "add_plan"
    ADD_PLAN_ENTRY = "add_plan_entry"
    UPDATE_PLAN = "update_plan"
    UPDATE_PLAN_ENTRY = "update_plan_entry"
    CLOSE_PLAN = "close_plan"
    DELETE_PLAN = "delete_plan"
    DELETE_PLAN_ENTRY = "delete_plan_entry"


class PROJECT:
    GET_PROJECT = "get_project"
    GET_PROJECTS = "get_projects"
    ADD_PROJECT = "add_project"
    UPDATE_PROJECT = "update_project"
    DELETE_PROJECT = "delete_project"


class RESULTS:
    GET_RESULTS = "get_results"
    GET_RESULTS_FOR_CASE = "get_results_for_case"
    GET_RESULTS_FOR_RUN = "get_results_for_run"
    ADD_RESULT = "add_result"
    ADD_RESULT_FOR_CASE = "add_results_for_case"
    ADD_RESULTS = "add_results"
    ADD_RESULTS_FOR_CASES = "add_results_for_cases"


class RUN:
    GET_RUN = "get_run"
    GET_RUNS = "get_runs"
    ADD_RUN = "add_run"
    UPDATE_RUN = "update_run"
    CLOSE_RUN = "close_run"
    DELETE_RUN = "delete_run"


class TEST:
    GET_TEST = "get_test"
    GET_TESTS = "get_tests"


class ATTACHMENT:
    ADD_ATTACHMENT_TO_RESULT = "get_attachment_to_result"
    GET_ATTACHMENTS_FOR_CASE = "get_attachments_for_case"
    GET_ATTACHMENTS_FOR_TEST = "get_attachments_for_test"
    GET_ATTACHMENT = "get_attachment"
    DELETE_ATTACHMENT = "delete_attachment"


class CASE:
    GET_CASE = "get_case"
    GET_CASES = "get_cases"
    ADD_CASE = "add_case"
    UPDATE_CASE = "update_case"
    DELETE_CASE = "delete_case"


class CASE_FIELDS:
    GET_CASE_FIELDS = "get_case_fields"
    ADD_CASE_FIELD = "add_case_field"


class CASE_TYPES:
    GET_CASE_TYPES = "get_case_types"


class CONFIGURATION:
    GET_CONFIGS = "get_configs"
    ADD_CONFIG_GROUP = "add_config_group"
    ADD_CONFIG = "add_config"
    UPDATE_CONFIG_GROUP = "update_config_group"
    UPDATE_CONFIG = "update_config"
    DELETE_CONFIG_GROUP = "delete_config_group"
    DELETE_CONFIG = "delete_config"


class PRIORITY:
    GET_PRIORITIES = "get_priorities"


class REPORT:
    GET_REPORTS = "get_reports"
    RUN_REPORT = "run_report"


class ResultFields:
    GET_RESULT_FIELDS = "get_result_fields"


class SECTION:
    GET_SECTION = "get_section"
    GET_SECTIONS = "get_sections"
    ADD_SECTION = "add_section"
    UPDATE_SECTION = "update_section"
    DELETE_SECTION = "delete_section"


class STATUSES:
    GET_STATUSES = "get_statuses"


class SUITES:
    GET_SUITE = "get_suite"
    GET_SUITES = "get_suites"
    ADD_SUITE = "add_suite"
    UPDATE_SUITE = "update_suite"
    DELETE_SUITE = "delete_suite"


class TEMPLATES:
    GET_TEMPLATES = "get_templates"


class USERS:
    GET_USER = "get_user"
    GET_USER_BY_EMAIL = "get_user_by_email"
    GET_USERS = "get_users"
