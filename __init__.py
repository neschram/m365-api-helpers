from enum import Enum
from typing import LiteralString


class UserQueryOptions(Enum):
    """Microsoft Graph SDK User properties enumeration.
    
    Name values are the python request variables, value values are the
    Microsoft query string vales.

    call `UserQueryOptions.choices()` to view the full list of choices.
    To get a specific name, value pair from the choices, use the first index
    from each of the returned choice tuples.

    Example:
        >>> UserQueryOptions.choices()[1]
        ('account_enabled', 'accountEnabled')
        >>> UserQueryOptions.account_enabled
        <UserQueryOptions.account_enabled: 'accountEnabled'>
        >>> UserQueryOptions.account_enabled.name
        'account_enabled'
        >>> UserQueryOptions.account_enabled.value
        'accountEnabled'
        >>> UserQueryOptions.to_request("accountEnabled")
        'account_enabled'
        >>> UserQueryOptions.to_prop("account_enabled")
        'accountEnabled'
        

    Attributes:
        id (LiteralString['id']): The unique identifier for the user.
        account_enabled (LiteralString['accountEnabled']): Indicates whether the account is enabled.
        age_group (LiteralString['ageGroup']): The age group of the user.
        assigned_Licenses (LiteralString['assignedLicenses']): The licenses assigned to the user.
        assigned_Plans (LiteralString['assignedPlans']): The plans assigned to the user.
        birthday (LiteralString['birthday']): The user's birthday.
        business_phones (LiteralString['businessPhones']): The user's business phone numbers.
        city (LiteralString['city']): The city in which the user is located.
        company_name (LiteralString['companyName']): The name of the company where the user works.
        consent_provided_for_minor (LiteralString['consentProvidedForMinor']): Indicates if consent is provided for minors.
        country (LiteralString['country']): The country in which the user is located.
        created_date_time (LiteralString['createdDateTime']): The date and time the user was created.
        creation_type (LiteralString['creationType']): The type of creation.
        department (LiteralString['department']): The department in which the user works.
        display_name (LiteralString['displayName']): The name displayed in the address book for the user.
        employee_id (LiteralString['employeeId']): The employee ID of the user.
        employee_hire_date (LiteralString['employeeHireDate']): The hire date of the user.
        employee_type (LiteralString['employeeType']): The type of employee.
        external_user_state (LiteralString['externalUserState']): The state of the external user.
        external_user_state_change_date_time (LiteralString['externalUserStateChangeDateTime']): The date and time of the external user state change.
        fax_number (LiteralString['faxNumber']): The user's fax number.
        give_name (LiteralString['givenName']): The user's first name.
        im_addresses (LiteralString['imAddresses']): The user's instant messaging addresses.
        job_title (LiteralString['jobTitle']): The user's job title.
        mail (LiteralString['mail']): The user's email address.
        mail_nickname (LiteralString['mailNickname']): The user's mail nickname.
        mobile_phone (LiteralString['mobilePhone']): The user's mobile phone number.
        office_location (LiteralString['officeLocation']): The location of the user's office.
        on_premises_immutable_id (LiteralString['onPremisesImmutableId']): The on-premises immutable ID.
        on_premises_last_sync_date_time (LiteralString['onPremisesLastSyncDateTime']): The last sync date and time for on-premises.
        on_premises_security_identifier (LiteralString['onPremisesSecurityIdentifier']): The on-premises security identifier.
        on_premises_sync_enabled (LiteralString['onPremisesSyncEnabled']): Indicates if on-premises sync is enabled.
        password_policies (LiteralString['passwordPolicies']): The password policies for the user.
        password_profile (LiteralString['passwordProfile']): The password profile for the user.
        postal_code (LiteralString['postalCode']): The postal code for the user.
        preferred_language (LiteralString['preferredLanguage']): The user's preferred language.
        preferred_name (LiteralString['preferredName']): The user's preferred name.
        provisioned_plans (LiteralString['provisionedPlans']): The provisioned plans for the user.
        proxy_addresses (LiteralString['proxyAddresses']): The proxy addresses for the user.
        responsibilities (LiteralString['responsibilities']): The user's responsibilities.
        schools (LiteralString['schools']): The schools attended by the user.
        skills (LiteralString['skills']): The user's skills.
        state (LiteralString['state']): The state in which the user is located.
        street_address (LiteralString['streetAddress']): The street address for the user.
        surname (LiteralString['surname']): The user's last name.
        usage_location (LiteralString['usageLocation']): The location where the user is using the service.
        user_principal_name (LiteralString['userPrincipalName']): The principal name for the user.
        user_type (LiteralString['userType']): The type of user.
    """

    id: LiteralString = "id"
    account_enabled: LiteralString = "accountEnabled"
    age_group: LiteralString = "ageGroup"
    assigned_Licenses: LiteralString = "assignedLicenses"
    assigned_Plans: LiteralString = "assignedPlans"
    birthday: LiteralString = "birthday"
    business_phones: LiteralString = "businessPhones"
    city: LiteralString = "city"
    company_name: LiteralString = "companyName"
    consent_provided_for_minor: LiteralString = "consentProvidedForMinor"
    country: LiteralString = "country"
    created_date_time: LiteralString = "createdDateTime"
    creation_type: LiteralString = "creationType"
    department: LiteralString = "department"
    display_name: LiteralString = "displayName"
    employee_id: LiteralString = "employeeId"
    employee_hire_date: LiteralString = "employeeHireDate"
    employee_type: LiteralString = "employeeType"
    external_user_state: LiteralString = "externalUserState"
    external_user_state_change_date_time: LiteralString = "externalUserStateChangeDateTime"
    fax_number: LiteralString = "faxNumber"
    give_name: LiteralString = "givenName"
    im_addresses: LiteralString = "imAddresses"
    job_title: LiteralString = "jobTitle"
    mail: LiteralString = "mail"
    mail_nickname: LiteralString = "mailNickname"
    mobile_phone: LiteralString = "mobilePhone"
    office_location: LiteralString = "officeLocation"
    on_premises_immutable_id: LiteralString = "onPremisesImmutableId"
    on_premises_last_sync_date_time: LiteralString = "onPremisesLastSyncDateTime"
    on_premises_security_identifier: LiteralString = "onPremisesSecurityIdentifier"
    on_premises_sync_enabled: LiteralString = "onPremisesSyncEnabled"
    password_policies: LiteralString = "passwordPolicies"
    password_profile: LiteralString = "passwordProfile"
    postal_code: LiteralString = "postalCode"
    preferred_language: LiteralString = "preferredLanguage"
    preferred_name: LiteralString = "preferredName"
    provisioned_plans: LiteralString = "provisionedPlans"
    proxy_addresses: LiteralString = "proxyAddresses"
    responsibilities: LiteralString = "responsibilities"
    schools: LiteralString = "schools"
    skills: LiteralString = "skills"
    state: LiteralString = "state"
    street_address: LiteralString = "streetAddress"
    surname: LiteralString = "surname"
    usage_location: LiteralString = "usageLocation"
    user_principal_name: LiteralString = "userPrincipalName"
    user_type: LiteralString = "userType"

    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]

    @classmethod
    def to_prop(cls, name: str):
        return getattr(cls, name).value
    
    @classmethod
    def to_request(cls, prop: str):
        for i in cls:
            if i.value == prop:
                return i.name
        raise KeyError(prop, "property not found for the given name")
