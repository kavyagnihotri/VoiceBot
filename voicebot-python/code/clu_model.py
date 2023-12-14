"""
FILE: clu_model.py

DESCRIPTION:
    This sample demonstrates how to analyze user query for intents and entities using
    a conversation project with a language parameter.

    For more info about how to setup a CLU conversation project, see the README.

USAGE:
    python sample_analyze_conversation_app.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_CONVERSATIONS_ENDPOINT                       - endpoint for your CLU resource.
    2) AZURE_CONVERSATIONS_KEY                            - API key for your CLU resource.
    3) AZURE_CONVERSATIONS_PROJECT_NAME     - project name for your CLU conversations project.
    4) AZURE_CONVERSATIONS_DEPLOYMENT_NAME  - deployment name for your CLU conversations project.
"""

from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

def get_top_topic(query, clu_endpoint, clu_key, clu_project_name, clu_deployment_name):
    # [START analyze_conversation_app]

    # get secrets
    # clu_endpoint = LANGUAGE_UNDERSTANDING_ENDPOINT
    # clu_key = LANGUAGE_UNDERSTANDING_KEY
    # project_name = CLU_PROJECT_NAME
    # deployment_name = CLU_DEPLOYMENT_NAME

    # analyze quey
    client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))
    with client:
        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": query
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": clu_project_name,
                    "deploymentName": clu_deployment_name,
                    "verbose": True
                }
            }
        )

    # view result
    print(f"query: {result['result']['query']}")
    # print(f"project kind: {result['result']['prediction']['projectKind']}\n")

    # print(f"top intent: {result['result']['prediction']['topIntent']}")
    # print(f"category: {result['result']['prediction']['intents'][0]['category']}")
    # print(f"confidence score: {result['result']['prediction']['intents'][0]['confidenceScore']}\n")

    # print("entities:")
    # for entity in result['result']['prediction']['entities']:
    #     print(f"\ncategory: {entity['category']}")
    #     print(f"text: {entity['text']}")
    #     print(f"confidence score: {entity['confidenceScore']}")
    #     if "resolutions" in entity:
    #         print("resolutions")
    #         for resolution in entity['resolutions']:
    #             print(f"kind: {resolution['resolutionKind']}")
    #             print(f"value: {resolution['value']}")
    #     if "extraInformation" in entity:
    #         print("extra info")
    #         for data in entity['extraInformation']:
    #             print(f"kind: {data['extraInformationKind']}")
    #             if data['extraInformationKind'] == "ListKey":
    #                 print(f"key: {data['key']}")
    #             if data['extraInformationKind'] == "EntitySubtype":
    #                 print(f"value: {data['value']}")

    # [END analyze_conversation_app]
    top_intent = result['result']['prediction']['entities'][0]['text']
    return top_intent
