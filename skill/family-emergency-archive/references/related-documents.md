# Related-document rules

Use these rules in Step 5 of the Skill. When a document in the left column is Found (or the user confirms the situation), add the documents in the right column to the checklist for the same member or household, if they are not already on it. In the report, show each added item with its reason, for example "Vehicle insurance (because vehicle registration was found)".

| If this is found or confirmed | Then also expect | Applies to |
|---|---|---|
| Vehicle registration | Vehicle insurance; driver licence for the main driver | household; each driver |
| Property deed or mortgage statement | Home insurance | household |
| Lease agreement, user is the tenant | Bond or deposit receipt; move-in condition report; **dated condition photos of the property** | household |
| Lease agreement, user is the landlord | Landlord insurance; bond or deposit record; condition report and **dated condition photos for each tenancy** | household, per rental property |
| Any child in the household | Birth certificate; vaccination record; guardianship nomination | each child; household |
| Life insurance policy | Beneficiary nomination; will | the policy holder |
| Pension or retirement account | Beneficiary nomination | the account holder |
| Will | Executor name in the emergency contact list | household |
| Regular medication in a medical report | Current medication and allergy list | that member |

## Condition photos check

Condition photos are the evidence a tenant or landlord needs if there is a dispute when a tenancy ends. For every lease found:

1. Take the lease start date (and end date, if the tenancy has ended) from the extracted lease fields.
2. Ask `photo-agent` for photos in the confirmed folders taken from 14 days before to 14 days after each date.
3. If photos exist, mark "Condition photos" as Found and give the folder or album and the photo count. If none exist, mark it Missing and explain why it matters in one line.

The Skill only checks that dated photos exist. It does not judge the condition of the property.
