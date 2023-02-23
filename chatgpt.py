import openai
import urllib3
import json

# openai.organization = "org-mi4nAQjBsG2HIOjMDnHcykg7" #personal
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.Model.list()

"""
curl https://api.openai.com/v1/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'
"""
timeout = urllib3.Timeout(connect = 5.0, read = 20.0)
http = urllib3.PoolManager(timeout = timeout)

def chatgpt(prompt):
    prompt = prompt.encode('utf-8').decode("latin1") #for encoding problem. support chinese 
    data = {"model" : "text-davinci-003", 
            "prompt" : prompt, 
            "temperature" : 0, 
            "max_tokens" : 4096 - len(prompt), 
            "n" : 1}
    encoded_data = json.dumps(data, ensure_ascii = False)

    try:
        r = http.request('POST','https://api.openai.com/v1/completions',
            body = encoded_data,
            headers = {'Content-Type': 'application/json', 'Authorization': '{YOUR KEY}'})
        res = json.loads(r.data)
        status = r.status
        if (status != 200):
            return status, res["error"]["message"]
        else:
            return status, res["choices"][0]["text"]
    except Exception as e:
        return -1, str(e)
