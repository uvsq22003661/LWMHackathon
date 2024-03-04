from openai import OpenAI
import os
import traceback
import time

def generate(messages, **kwargs):
    client = OpenAI()
    result = None
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        try:
            result = client.chat.completions.create(messages=messages, **kwargs)
            break
        except Exception:
            traceback.print_exc()
            waiting_time = 5
            print(f'\nGPT exception. Trying again in {waiting_time} seconds ...')
            time.sleep(waiting_time)
            attempts += 1

    return result.choices[0].message.content

def inspireMe():
    chat_kwargs = {
        'model': 'gpt-3.5-turbo-0125',#'gpt-4-0125-preview',#'gpt-3.5-turbo-0125',
        'temperature': 1.2,
        'max_tokens': 512
    }

    user_request = input("Describe the subject of your research in a few lines :")

    prompt = [
        {
            "role": "system",
            "content": "You are a well known searcher with a deep understanding of computer sciences. A searcher comes to see you in your office. First the searcher describes to you what the subject of his research is. You need to help him structure his research. Give him an example of a good plan for his paper."
        },
        {
            "role": "user",
            "content": "I am working on a thesis about a cryptosecure voting system."
        },
        {
            "role": "assistant",
            "content": "1. Introduction \n    - Introduce the concept of cryptosecure voting systems.\n    - Highlight the importance of secure and trustworthy voting mechanisms in democratic societies.\n    - Provide an overview of the current challenges and vulnerabilities in traditional voting systems.\n    - State the objectives and scope of your research.\n2. Literature Review\n    - Review the existing literature on cryptosecure voting systems, cryptographic techniques, and related technologies.\n    - Discuss previous research efforts and their findings in the field.\n    - Identify gaps in the existing literature and explain how your research fills these gaps.\n3. Background and Concepts\n    - Provide background information on voting systems and their requirements.\n    - Explain the fundamental concepts of cryptography relevant to voting systems, such as encryption, digital signatures, and homomorphic encryption.\n    - Discuss the principles of cryptosecure voting systems and the challenges they aim to address.\n4. Design and Implementation\n    - Present the design principles of your cryptosecure voting system.\n    - Describe the architecture and components of the system.\n    - Explain the cryptographic techniques and protocols used to ensure security, privacy, and verifiability.\n    - Detail the implementation of the system, including software development and integration with existing voting infrastructure.\n5. Security Analysis\n    - Conduct a comprehensive security analysis of your cryptosecure voting system.\n    - Identify potential threats and vulnerabilities.\n    - Discuss the effectiveness of the cryptographic mechanisms in mitigating these threats.\n    - Present the results of security assessments, including penetration testing and formal verification.\n6. Evaluation and Validation\n    - Describe the methods used to evaluate the performance and usability of your cryptosecure voting system.\n    - Present empirical results from simulations, prototypes, or real-world deployments.\n    - Discuss user feedback and observations from usability studies.\n    - Validate the security properties and correctness of the system through formal proofs or empirical evidence.\n7. Case Studies and Use Cases\n    - Provide case studies or examples of how your cryptosecure voting system could be applied in different contexts.\n    - Discuss real-world use cases and scenarios where the system could be deployed.\n    - Analyze the potential impact of the system on election integrity, voter trust, and democratic processes.\n8. Discussion\n    - Summarize the key findings and contributions of your research.\n    - Reflect on the strengths and limitations of your cryptosecure voting system.\n    - Discuss the implications of your research for the field of cryptosecurity and voting systems.\n    - Identify future research directions and areas for improvement.\n9. Conclusion\n    - Recapitulate the main points of your thesis.\n    - Reiterate the significance of your research in the context of secure voting systems.\n    - Offer concluding remarks and suggestions for further work.\n10. References\n    - Provide a comprehensive list of references cited throughout your thesis.\nRemember to tailor this structure to fit the specific requirements of your institution and the depth of your research. Good luck with your thesis! If you need further clarification or assistance with any section, feel free to ask."
        },
        {
            "role":"user",
            "content": user_request
        }
    ]

    response = generate(prompt, **chat_kwargs)
    print(response)
    

OPENAI_API_KEY = "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"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

runing = True
while runing:
    users_input = input("Hi! Welcome to HelpMyProject, the first command line tool designed to help researchers!\n 1:Who With ?\n 2:Inspire me\n 3:Fund me\n 4:Leave\n")    
    if users_input=="1":
        pass
    elif users_input=="2":
        inspireMe()
    elif users_input=="3":
        pass
    elif users_input=="4":
        runing=False