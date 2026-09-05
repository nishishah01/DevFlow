from langgraph.graph import StateGraph, END

from app.graph.state import DevFlowState


def build_graph():

    graph = StateGraph(DevFlowState)

    graph.add_node(
        "triage",
        triage_agent
    )

    graph.add_node(
        "context",
        context_agent
    )

    graph.add_node(
        "planner",
        planner_agent
    )

    graph.add_node(
        "coder",
        coder_agent
    )

    graph.add_node(
        "tester",
        tester_agent
    )

    graph.add_node(
        "reviewer",
        reviewer_agent
    )

    graph.set_entry_point("triage")

    graph.add_edge(
        "triage",
        "context"
    )

    graph.add_edge(
        "context",
        "planner"
    )

    graph.add_edge(
        "planner",
        "coder"
    )

    graph.add_edge(
        "coder",
        "tester"
    )

    graph.add_conditional_edges(
        "tester",
        should_retry,
        {
            "retry": "coder",
            "review": "reviewer",
            "human": END,
        }
    )

    graph.add_edge(
        "reviewer",
        END
    )

    return graph.compile()