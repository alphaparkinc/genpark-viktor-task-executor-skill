from client import ViktorTaskExecutorClient
client = ViktorTaskExecutorClient()
result = client.execute(
    task_description="Research the top 5 competitors and compile a comparison table with pricing and features",
    tools_available=["browser", "spreadsheet", "document"]
)
print(f"Status: {result['completion_status']}")
print(f"Artifacts: {[a['id'] for a in result['artifacts']]}")
for step in result["execution_steps"]:
    print(f"  Step {step['step']}: [{step['action']}] {step['detail']}")
