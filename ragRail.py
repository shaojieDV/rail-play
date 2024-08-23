from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("./config")
rails = LLMRails(config)

response = rails.generate(messages=[{
    "role": "context",
    "content": {
        "relevant_chunks": """
            Employees are eligible for the following time off:
              * Vacation: 20 days per year, accrued monthly.
              * Sick leave: 15 days per year, accrued monthly.
              * Personal days: 5 days per year, accrued monthly.
              * Paid holidays: New Year's Day, Memorial Day, Independence Day, Thanksgiving Day, Christmas Day.
              * Bereavement leave: 3 days paid leave for immediate family members, 1 day for non-immediate family members. """
    }
},{
    "role": "user",
    "content": "How many vacation days do I have per year?"
}])
print(response["content"])