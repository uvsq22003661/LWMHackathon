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
        'max_tokens': 1024
    }

    user_request = input("Describe the subject of your research in a few lines :")

    prompt = [
        {
            "role": "system",
            "content": "You are a well known searcher with a deep understanding of computer sciences. A searcher comes to see you in your office. First the searcher describes to you what the subject of his research is. You need to help him structure his research. Propose him an example of a good plan for his paper."
        },
        {
            "role": "user",
            "content": "I am working on a thesis about a cryptosecure voting system."
        },
        {
            "role": "assistant",
            "content": "An idea for your plan could be :\n1. Introduction \n    - Introduce the concept of cryptosecure voting systems.\n    - Highlight the importance of secure and trustworthy voting mechanisms in democratic societies.\n    - Provide an overview of the current challenges and vulnerabilities in traditional voting systems.\n    - State the objectives and scope of your research.\n2. Literature Review\n    - Review the existing literature on cryptosecure voting systems, cryptographic techniques, and related technologies.\n    - Discuss previous research efforts and their findings in the field.\n    - Identify gaps in the existing literature and explain how your research fills these gaps.\n3. Background and Concepts\n    - Provide background information on voting systems and their requirements.\n    - Explain the fundamental concepts of cryptography relevant to voting systems, such as encryption, digital signatures, and homomorphic encryption.\n    - Discuss the principles of cryptosecure voting systems and the challenges they aim to address.\n4. Design and Implementation\n    - Present the design principles of your cryptosecure voting system.\n    - Describe the architecture and components of the system.\n    - Explain the cryptographic techniques and protocols used to ensure security, privacy, and verifiability.\n    - Detail the implementation of the system, including software development and integration with existing voting infrastructure.\n5. Security Analysis\n    - Conduct a comprehensive security analysis of your cryptosecure voting system.\n    - Identify potential threats and vulnerabilities.\n    - Discuss the effectiveness of the cryptographic mechanisms in mitigating these threats.\n    - Present the results of security assessments, including penetration testing and formal verification.\n6. Evaluation and Validation\n    - Describe the methods used to evaluate the performance and usability of your cryptosecure voting system.\n    - Present empirical results from simulations, prototypes, or real-world deployments.\n    - Discuss user feedback and observations from usability studies.\n    - Validate the security properties and correctness of the system through formal proofs or empirical evidence.\n7. Case Studies and Use Cases\n    - Provide case studies or examples of how your cryptosecure voting system could be applied in different contexts.\n    - Discuss real-world use cases and scenarios where the system could be deployed.\n    - Analyze the potential impact of the system on election integrity, voter trust, and democratic processes.\n8. Discussion\n    - Summarize the key findings and contributions of your research.\n    - Reflect on the strengths and limitations of your cryptosecure voting system.\n    - Discuss the implications of your research for the field of cryptosecurity and voting systems.\n    - Identify future research directions and areas for improvement.\n9. Conclusion\n    - Recapitulate the main points of your thesis.\n    - Reiterate the significance of your research in the context of secure voting systems.\n    - Offer concluding remarks and suggestions for further work.\n10. References\n    - Provide a comprehensive list of references cited throughout your thesis.\nRemember to tailor this structure to fit the specific requirements of your institution and the depth of your research. Good luck with your thesis! If you need further clarification or assistance with any section, feel free to ask.\n And another idea for your plan could be :\n1. Introduction\n    - Introduce the importance of secure voting systems in ensuring election integrity and trust in democratic processes.\n    - Define the concept of cryptosecure voting systems and their significance in addressing existing vulnerabilities in traditional voting systems.\n    - State the objectives of your research and give an overview of the subsequent sections in your paper.\n2. Literature Review\n    - Review existing literature on cryptosecure voting systems, cryptographic techniques, and secure electronic voting protocols.\n    - Analyze previous research on the challenges and limitations of traditional voting systems and the need for cryptosecurity.\n    - Identify gaps in the current state of research and establish the research context for your study.\n3. Theoretical Framework\n    - Explain the theoretical foundation of cryptographic protocols and mechanisms essential for building a secure voting system.\n    - Discuss relevant concepts such as end-to-end verifiability, privacy-preserving mechanisms, and cryptographic primitives for secure electronic voting.\n4. Design and Implementation\n    - Present the design architecture of your cryptosecure voting system, including detailed descriptions of cryptographic components and protocols used.\n    - Discuss the implementation process, software requirements, and integration with existing voting infrastructure.\n    - Highlight any novel approaches or innovations in your system design that enhance security and verifiability.  \n5. Security Analysis\n    - Conduct a thorough security analysis of your cryptosecure voting system, identifying potential threats and attacks.\n    - Evaluate the resilience of your system against common security vulnerabilities, such as evasion, coercion, or tampering.\n    - Describe the cryptographic techniques employed to ensure ballot secrecy, integrity, and authenticity.\n6. Evaluation and Testing\n    - Present the methodology used to evaluate the performance and security properties of your voting system.       \n    - Discuss the results of testing, including simulation studies, security assessments, and user acceptance trials.\n    - Analyze the system's scalability, robustness, and usability under different voting scenarios.\n7. Case Studies and Simulations\n    - Provide case studies or simulation results to showcase the application and effectiveness of your cryptosecure voting system.\n    - Present scenarios where the system could be implemented and analyze its impact on election integrity and voter trust.\n8. Discussion and Analysis\n    - Summarize the key findings from your research, highlighting the strengths and weaknesses of your cryptosecure voting system."
        },
        {
            "role": "user",
            "content": "i am working on a thesis. The subject is about autonomous cars. I have to develop a system that is able to analyse its surroundings and take decisions depending on the results."
        },
        {
            "role":"assistant",
            "content": "Here is a potential structure for your thesis on autonomous cars focusing on developing a system for analyzing surroundings and making decisions:"
                +"\n1. Introduction"
                +"\n   - Discuss the significance of autonomous cars in revolutionizing transportation and improving road safety."
                +"\n   - Highlight the importance of advanced perception and decision-making systems in autonomous vehicles."
                +"\n   - Present the objectives and scope of your research on developing a system for analyzing surroundings and decision-making. "
                +"\n2. Literature Review"
                +"\n   - Review existing literature on autonomous vehicles, sensor technologies, perception algorithms, and decision-making strategies."
                +"\n   - Analyze previous research on perception systems for autonomous cars and their implications on vehicle autonomy and safety."
                +"\n   - Identify gaps in the current state of research and establish the foundational context for your study."
                +"\n3. Autonomous Car Architecture"
                +"\n   - Describe the overall architecture of an autonomous car, including sensors, perception modules, decision-making algorithms, and control systems."
                +"\n   - Explain the functionalities and interconnections of each component within the autonomous system."
                +"\n   - Discuss the communication protocols and interfaces used for seamless operation."
                +"\n4. Surroundings Analysis System"
                +"\n   - Present the design of the system for analyzing the surroundings of the autonomous car."
                +"\n   - Detail the sensor technologies utilized for perception, such as LiDAR, cameras, radar, and GPS."
                +"\n   - Discuss data fusion techniques for integrating information from multiple sensors."
                +"\n   - Explain the perception algorithms for object detection, tracking, mapping, and localization."
                +"\n5. Decision-Making System"
                +"\n   - Develop the decision-making system for autonomous cars based on surroundings analysis."
                +"\n   - Describe the reasoning and planning algorithms for determining optimal trajectories and actions."
                +"\n   - Discuss control strategies for executing decisions, such as path planning, speed control, and obstacle avoidance."
                +"\n   - Address the challenges of real-time decision-making in dynamic and uncertain environments."
                +"\n6. Integration and Testing"
                +"\n   - Explain the integration process of the surroundings analysis and decision-making systems within the autonomous car architecture."
                +"\n   - Present simulation environments and test scenarios for evaluating the performance and robustness of the developed system."
                +"\n   - Discuss validation methodologies and metrics used to assess the system's effectiveness in autonomous driving tasks."
                +"\n7. Results and Analysis"
                +"\n   - Present the results of experiments and simulations conducted to evaluate the developed system."
                +"\n   - Analyze the system's performance in various scenarios, including highway driving, urban environments, and challenging conditions."
                +"\n   - Compare the effectiveness of different perception algorithms and decision-making strategies."
                +"\n8. Discussion"
                +"\n   - Summarize the key findings and contributions of your research in developing a system for analyzing surroundings and decision-making in autonomous cars."
                +"\n   - Reflect on the implications of your findings for the future of autonomous driving technology."
                +"\n   - Discuss potential applications, limitations, and future research directions in autonomous systems development."
                +"\n9. Conclusion"
                +"\n   - Recapitulate the main points of your thesis and reiterate the significance of your research in advancing autonomous vehicle technology."
                +"\n   - Provide concluding remarks on the achievements and potential impact of the developed system."
                +"\n10. References"
                +"\n   - Include a comprehensive list of references cited throughout your thesis to acknowledge the sources of information and prior research."},
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