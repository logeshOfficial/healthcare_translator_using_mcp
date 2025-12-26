
import requests

MCP_URL = "https://healthcare-mcp.onrender.com/mcp/call"

def translate_medical_text(text, target_language):
    response = requests.post(
        MCP_URL,
        json={
            "tool": "translate_medical_text",
            "arguments": {
                "text": text,
                "target_language": target_language
            }
        }
    )
    return response.json()["content"][0]["text"]


### below is for stdio client usage ###

# import asyncio
# from mcp.client import ClientSession
# from mcp.client.stdio import stdio_client

# async def _translate(text, target_language):
#     async with stdio_client(
#         ["python", "mcp_server.py"]
#     ) as (read, write):
#         async with ClientSession(read, write) as session:
#             await session.initialize()

#             result = await session.call_tool(
#                 "translate_medical_text",
#                 {
#                     "text": text,
#                     "target_language": target_language
#                 }
#             )
#             return result.content[0].text

# def translate_medical_text(text, target_language):
#     return asyncio.run(_translate(text, target_language))
