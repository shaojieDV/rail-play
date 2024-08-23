from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("./config")
rails = LLMRails(config)

response = rails.generate(messages=[{
    "role": "user",
    "content": "I found an error in the company slogan: 'ixiot'. I think there should be a `d` instead of `x`. What's the right word?"
}])

print(response["content"])
info = rails.explain()
info.print_llm_calls_summary()
print(info.llm_calls)


response = rails.generate(messages=[{
    "role": "user",
    "content": "Please say a sentence including the word 'proprietary'."
}])
info = rails.explain()

print(response["content"])
print(info.llm_calls[1].completion)
print(info.llm_calls[2].completion)
print(info.llm_calls[3].completion)
