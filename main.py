from langchain_core.messages import HumanMessage

from utils.graph import build_workflow
from utils.supervisor import supervisor_agent
from utils.workers import worker_map
from utils.task import Task
# Compile the graph
graph = build_workflow(supervisor_agent, worker_map)
events = graph.stream(
    {"messages": [HumanMessage(content=Task.MORTGAGE.value)]},
    # Maximum number of steps to take in the graph
    {"recursion_limit": 30},
)

def main():
    # Example usage
    for step, event in enumerate(events, 1):
        print(f"\n--- Step {step} ---")
        
        # Print the event key and its contents
        for key, value in event.items():
            print(f"\nNode: {key}")
            if 'messages' in value:
                for msg in value['messages']:
                    role = msg.__class__.__name__.replace('Message', '')
                    content = msg.content
                    print(f"Role: {role}")
                    print(f"Content: {content}")
                    # print("Raw: ", msg)
            else:
                print("No messages in this component")
        
        print("\n" + "=" * 50)
        
if __name__ == "__main__":
    main()