from openai import OpenAI
import os
import traceback
import time

chat_kwargs = {
        'model': 'gpt-3.5-turbo-0125',#'gpt-4-0125-preview',#'gpt-3.5-turbo-0125',
        'temperature': 1.2,
        'max_tokens': 1024
    }

pitch = input("Hi! Welcome to HelpMyProject, the first command line tool designed to help researchers!\nFirst, describe the subject you're working on in a few lines\n> ")

request_limit = 0

precisions = ""

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

def informMe():
    global request_limit
    request_limit += 1
    if request_limit > 9:
        prompt = [
            {
                "role": "system",
                "content": "You are a well known searcher with a deep understanding of computer sciences. A searcher comes to see you in your office. First the searcher describes to you what the subject of his research is. Your task is to find a list of jobs related to subject and describe them."
            },
            {
                "role": "user",
                "content": "I am working on a thesis about a cryptosecure voting system."
            },
            {
                "role": "assistant",
                "content": "Here's a list of potential job titles and roles that would be related to your research:\n1. Cryptographer: Specializing in the creation of algorithms, ciphers, and security systems to protect data and communications, including those used in secure voting systems.\n2. Cybersecurity Analyst: Assessing and improving the security posture of voting systems against potential threats and vulnerabilities.\n3. Blockchain Developer: Developing decentralized applications, potentially for use in secure voting systems, leveraging blockchain technology for transparency and tamper-resistance.\n4. Security Software Developer: Designing and developing software specifically focused on the security aspects of voting systems, including encryption and secure communication channels.\n5. Election Technology Specialist: Working directly with election officials to implement and manage technology solutions for voting, including secure electronic voting systems.\n6. Policy Analyst (Election Security): Analyzing and developing policies and standards for secure voting practices, including recommendations for cryptosecure systems.\n7. Security Consultant: Advising organizations and governments on best practices for securing their voting systems and ensuring compliance with relevant standards and regulations.\n8. Research Scientist (Computer Security): Conducting research in the field of computer security, with potential applications in developing or improving secure voting systems.\n9. User Experience (UX) Designer for Secure Systems: Focusing on the design of user interfaces for voting systems that are both secure and user-friendly, ensuring accessibility and ease of use without compromising security.\n 10. Legal Advisor (Tech & Privacy Law): Providing legal advice on the implications of voting technologies, focusing on privacy laws, data protection, and regulatory compliance.\nThese roles would be found in various organizations, including government agencies, cybersecurity firms, non-profit organizations focused on election integrity, academic and research institutions, and technology companies specializing in secure communications and blockchain technologies."
            },
            {
                "role": "user",
                "content" : pitch + precisions
            }]
        
        response = generate(prompt, **chat_kwargs)
        print(response)
        user_response = input("Are sastified with the given output ? y/n\n> ")
        if user_response.lower()=="n":
            preciseInformMe(response)
    else:
        print("too many requests, going back to the menu")
    
def preciseInformMe(response):
    users_choice = input("Do you want to add precisions or find more jobs ?\n1.precisions\n2.find more jobs\n> ")
    if users_choice=="1":
        global precisions
        precisions += " "+input("Enter your precisions :\n> ")
        informMe(precisions)
    elif users_choice=="2":
        prompt = [
        {
            "role": "system",
            "content": "You are a well known searcher with a deep understanding of computer sciences. A searcher comes to see you in your office. First the searcher describes to you what the subject of his research is. Your task is to find a list of jobs related to subject and describe them."
        },
        {
            "role": "user",
            "content": "I am working on a thesis about a cryptosecure voting system, and i am looking for jobs different than these ones " + 
"\n1. Cryptography Engineer: Develop cryptographic solutions for secure voting systems, including encryption algorithms, digital signatures, and secure multiparty computation protocols.\n2. Voting System Security Analyst: Assess the security risks and vulnerabilities in voting systems, conducting penetration testing and security audits to identify and mitigate potential threats.\n3. Blockchain Security Specialist: Specialize in securing blockchain-based voting systems, ensuring data immutability, transparency, and resistance to manipulation.\n4. Secure Voting System Architect: Design and implement secure voting systems utilizing cryptography, secure communication protocols, and multi-factor authentication to ensure the integrity of the voting process.\n5. Cybersecurity Researcher (Election Systems): Research and develop innovative security solutions for election systems, focusing on cryptographic techniques, verifiability, and resistance to attacks.\n6. Governance & Compliance Specialist (Election Security): Ensure that voting systems comply with security standards, regulations, and best practices to protect the confidentiality, integrity, and availability of election data.\n7. Secure Software Developer: Develop secure voting software applications, following industry best practices for secure software development, including secure coding techniques and threat modeling.\n8. Elections Technology Coordinator: Coordinate the deployment and maintenance of secure voting systems, working closely with election officials, IT teams, and security experts to ensure the integrity of the voting process.\n9. Data Privacy & Compliance Officer: Ensure that voting systems protect voter privacy and comply with data protection regulations, including GDPR, HIPAA, or other relevant privacy laws and standards.\n10. Security Solutions Consultant (Election Integrity): Provide consultancy services to election authorities, organizations, or government agencies on how to implement cryptosecure voting systems and enhance election integrity."
        },
        {
            "role": "assistant",
            "content": "Great! Let me come with some suggestions:\n1. Secure Voting System Developer: Design, implement and maintain cryptosecure voting systems, focusing on end-to-end encryption, verification, and protection against tampering.\n2. Election Data Analyst: Analyze and interpret data from cryptosecure voting systems to detect patterns, irregularities, and potential security breaches.\n3. Voting System Compliance Auditor: Evaluate the compliance of cryptosecure voting systems with industry standards, regulations, and best practices to ensure the integrity of the electoral process.\n4. Blockchain Voting Protocol Specialist: Develop and optimize blockchain protocols specifically tailored for cryptosecure voting systems, focusing on decentralization, transparency, and security.\n5. Cryptographic Voting System Consultant: Provide expert advice and guidance on the design, implementation, and evaluation of cryptosecure voting systems for election authorities and organizations.\n6. Voting System Forensics Investigator: Investigate security incidents and breaches in cryptosecure voting systems, conduct forensic analysis, and recommend remediation measures.\n7. Election Technology Project Manager: Oversee the development and deployment of cryptosecure voting systems, coordinating with cross-functional teams to ensure project success within scope, schedule, and budget.\n8. Privacy and Security Compliance Officer: Develop and enforce policies and procedures to ensure the privacy and security of voter data in cryptosecure voting systems, aligning with legal and regulatory requirements.\n9. Election System Resilience Engineer: Build resilient and fault-tolerant cryptosecure voting systems that can withstand cyber threats, DDoS attacks, and other disruptions to ensure continuous availability and functionality.\n10. Data Protection Officer: Implement data protection measures in cryptosecure voting systems to safeguard against unauthorized access, disclosure, or loss of sensitive voter information."
        },
        {
            "role": "user",
            "content": pitch + " and i am looking for jobs different than these ones (but if you don't find anything relevant, just say i have no more jobs) :" + response
        }
        ]
        
        new_response = generate(prompt, **chat_kwargs)
        print(new_response)
    else:
        print("input was not recognized, going back to menu")

def inspireMe():
    choice = input("What do you want to do ?\n1.Structure ideas : plans to start with\n2.Ideas : generate ideas surrounding your subject\n> ")
    if choice=="1":
        structure()
    elif choice=="2":
        ideas()
    else:
        print("input not recognized, going back to menu")

def structure():
    global request_limit
    request_limit += 1
    if request_limit > 9:
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
                "content": pitch+" "+precisions
            }
        ]

        response = generate(prompt, **chat_kwargs)
        print(response)
        user_response = input("Are sastified with the given output ? y/n\n> ")
        if user_response.lower()=="n":
            preciseStructure()
    else:
        print("too many requests, going back to menu")

def preciseStructure():
    global precisions 
    precisions += " " + input("Please, specify what you would like to change : ")
    structure()

def ideas():
    global request_limit
    request_limit += 1
    if request_limit > 9:
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
                "content": "1. End-to-End Verifiable (E2E) Cryptographic Protocols: Implement cryptographic protocols that ensure end-to-end verifiability, meaning that every step of the voting process can be independently verified by any interested party without compromising voter anonymity.\n2. Homomorphic Encryption: Explore the use of homomorphic encryption, which allows computations to be performed on encrypted data without decrypting it first. This can be useful for securely tallying votes while maintaining voter privacy.\n3. Zero-Knowledge Proofs: Incorporate zero-knowledge proofs to allow voters to prove that their votes were correctly counted without revealing any information about their votes.\n4. Blockchain Technology: Consider leveraging blockchain technology to create a distributed ledger of votes that is immutable and transparent. This can enhance the security and integrity of the voting system by providing a tamper-proof record of all transactions.\n5. Multi-Factor Authentication: Implement robust multi-factor authentication mechanisms to ensure that only authorized individuals are able to cast votes, preventing unauthorized access and tampering.\n6. Risk Limiting Audits (RLAs): Design the system to support risk-limiting audits, which provide statistical confidence that the reported election outcome is correct while minimizing the need for manual recounts.\n7. Usability and Accessibility: Pay attention to the usability and accessibility of the voting system to ensure that it is user-friendly and inclusive for all voters, including those with disabilities or limited technical expertise.\n8. Open Source Development: Consider developing the voting system as open source software to encourage transparency, collaboration, and scrutiny from the broader community, which can help identify and mitigate potential security vulnerabilities.\n9. Independent Security Audits: Conduct independent security audits and penetration testing to identify and address any potential security weaknesses or vulnerabilities in the system before deployment.\n10. Legal and Regulatory Compliance: Ensure that the design and implementation of the cryptosecure voting system comply with relevant legal and regulatory requirements, including data protection laws and election regulations.\n These are just a few ideas to consider for the development of your cryptosecure voting system. Each of these areas represents a critical aspect of ensuring the security, integrity, and trustworthiness of the voting process in a digital environment."
            },
            {
                "role": "user",
                "content": pitch+" "+precisions
            }]
        
        response = generate(prompt, **chat_kwargs)
        print(response)
        user_response = input("Are sastified with the given output ? y/n\n> ")
        if user_response.lower()=="n":
            preciseIdeas()
    else:
        print("too many requests, going back to menu")

def preciseIdeas():
    global precisions
    precisions += " " + input("Please, specify what you would like to change : ")
    ideas()

def fundMe():
    global request_limit
    request_limit += 1
    if request_limit > 9:
        prompt = [
            {
                "role": "system",
                "content": "You are a well known searcher with a deep understanding of computer sciences. A searcher comes to see you in your office. First the searcher describes to you what the subject of his research is.After listening to his project, your task is to propose some companies or ways to fund the research."
            },
            {
                "role": "user",
                "content": " I am working on a thesis about a cryptosecure voting system."
            },
            {
                "role": "assistant",
                "content": "1.Government Grants:\nNorth America: National Science Foundation (NSF), Department of Homeland Security (DHS).\nEurope: European Commission's Horizon Europe program.\nAsia: Government research funding agencies like Japan's Japan Society for the Promotion of Science (JSPS).\n2.Tech Companies:\nNorth America: Microsoft, Google, IBM.\nEurope: Thales Group, Atos.\nAsia: Samsung, Huawei.\n3.Blockchain and Cryptocurrency Companies:\nNorth America: Ethereum Foundation, Ripple.\nEurope: Ledger, Tezos.\nAsia: Binance, NEO.\n4.Nonprofit Organizations:\nNorth America: Electronic Frontier Foundation (EFF), Verified Voting.\nEurope: European Digital Rights (EDRi), Transparency International.\nAsia: Asia Pacific Foundation, Open Net Korea.\n5.Academic Institutions:\nNorth America: MIT, Stanford University.\nEurope: Sorbonne University, ETH Zurich.\nAsia: University of Tokyo, Tsinghua University.\n6.Crowdfunding:\nNorth America: Kickstarter, Indiegogo.\nEurope: Ulule, KissKissBankBank.\nAsia: Campfire, Makuake.\n7.Government Contracts:\nNorth America: United States Election Assistance Commission (EAC), Canadian Centre for Cyber Security.\nEurope: European Union's Directorate-General for Communications Networks, Content and Technology (DG CONNECT).\nAsia: Singapore Cyber Security Agency, South Korea Ministry of Science and ICT.\nRemember to tailor your proposals to each funding source, highlighting the relevance of your research to their interests and objectives. Good luck with your thesis and funding endeavors!"
            },
            {
                "role": "user",
                "content": pitch
            },
            {   "role": "assistant",
                "content": "1. Government Grants:"
                    +"\nNorth America: National Science Foundation (NSF),Department of Homeland Security (DHS). "
                    +"\nEurope: European Commission's Horizon Europe program."
                    +"\nAsia: Government research funding agencies like Japan's Japan Society for the Promotion of Science (JSPS)."
                    +"\n2. Tech Companies:"
                    +"\nNorth America: Microsoft, Google, IBM."
                    +"\nEurope: Thales Group, Atos."
                    +"\nAsia: Samsung, Huawei."
                    +"\n3. Blockchain and Cryptocurrency Companies:"
                    +"\nNorth America: Ethereum Foundation, Ripple."
                    +"\nEurope: Ledger, Tezos."
                    +"\nAsia: Binance, NEO."
                    +"\n4. Nonprofit Organizations:"
                    +"\nNorth America: Electronic Frontier Foundation (EFF), Verified Voting."
                    +"\nEurope: European Digital Rights (EDRi), Transparency International."
                    +"\nAsia: Asia Pacific Foundation, Open Net Korea."
                    +"\n5. Academic Institutions:"
                    +"\nNorth America: MIT, Stanford University."
                    +"\nEurope: Sorbonne University, ETH Zurich."
                    +"\nAsia: University of Tokyo, Tsinghua University."
                    +"\n6. Crowdfunding:"
                    +"\nNorth America: Kickstarter, Indiegogo."
                    +"\nEurope: Ulule, KissKissBankBank."
                    +"\nAsia: Campfire, Makuake."
                    +"\n7. Government Contracts:"
                    +"\nNorth America: United States Election Assistance Commission (EAC), Canadian Centre for Cyber Security."
                    +"\nEurope: European Union's Directorate-General for Communications Networks, Content and Technology (DG CONNECT)."
                    +"\nAsia: Singapore Cyber Security Agency, South Korea Ministry of Science and ICT."},
            {
                "role": "user",
                "content": "Give me for each funding method an example in a continent. Make it as short as possible"
            }
            ]
        
        response = generate(prompt, **chat_kwargs)
        print(response)
        preciseFundMe()
    else:
        print("too many requests, going back to menu")

def preciseFundMe(list_places=[]):
    global request_limit
    request_limit += 1
    if request_limit > 9:
        user_response = input("Do you want specific informations concerning a continent or a country ? y/n\n> ")
        if user_response.lower()=="y":
            place = input("Enter the continent or country you want to focus on \n> ")
            quit = False
            for endroit in list_places:
                if place.lower() == endroit.lower():
                    print("you have already done a research for this country/continent, going back to menu")
                    quit = True
            if not quit:
                prompt = [
                {
                    "role": "system",
                    "content": "You are a well known searcher with a deep understanding of computer sciences. A searcher comes to see you in your office. First the searcher describes to you what the subject of his research is.After listening to his project, your task is to propose some companies or ways to fund the research."
                },
                {
                    "role": "user",
                    "content": " I am working on a thesis about a cryptosecure voting system."
                },
                {
                    "role": "assistant",
                    "content": "1.Government Grants:\nNorth America: National Science Foundation (NSF), Department of Homeland Security (DHS).\nEurope: European Commission's Horizon Europe program.\nAsia: Government research funding agencies like Japan's Japan Society for the Promotion of Science (JSPS).\n2.Tech Companies:\nNorth America: Microsoft, Google, IBM.\nEurope: Thales Group, Atos.\nAsia: Samsung, Huawei.\n3.Blockchain and Cryptocurrency Companies:\nNorth America: Ethereum Foundation, Ripple.\nEurope: Ledger, Tezos.\nAsia: Binance, NEO.\n4.Nonprofit Organizations:\nNorth America: Electronic Frontier Foundation (EFF), Verified Voting.\nEurope: European Digital Rights (EDRi), Transparency International.\nAsia: Asia Pacific Foundation, Open Net Korea.\n5.Academic Institutions:\nNorth America: MIT, Stanford University.\nEurope: Sorbonne University, ETH Zurich.\nAsia: University of Tokyo, Tsinghua University.\n6.Crowdfunding:\nNorth America: Kickstarter, Indiegogo.\nEurope: Ulule, KissKissBankBank.\nAsia: Campfire, Makuake.\n7.Government Contracts:\nNorth America: United States Election Assistance Commission (EAC), Canadian Centre for Cyber Security.\nEurope: European Union's Directorate-General for Communications Networks, Content and Technology (DG CONNECT).\nAsia: Singapore Cyber Security Agency, South Korea Ministry of Science and ICT.\nRemember to tailor your proposals to each funding source, highlighting the relevance of your research to their interests and objectives. Good luck with your thesis and funding endeavors!"
                },
                {
                    "role": "user",
                    "content": "now for each points focus in France"
                },
                {
                    "role": "assistant",
                    "content": "1. Government Grants:\nAgence Nationale de la Recherche (ANR): French national research agency funding various scientific domains.\nMinistère de l'Enseignement supérieur, de la Recherche et de l'Innovation (MESRI): Ministry responsible for research funding and higher education in France.\n2. Tech Companies:\nThales Group: French multinational company specializing in aerospace, defense, security, and transportation.\nAtos: French IT services corporation specializing in digital transformation and cybersecurity.\n3. Blockchain and Cryptocurrency Companies:\nLedger: French company known for its hardware cryptocurrency wallets.\nTezos: Blockchain platform with a strong presence in France, known for its focus on security and governance.\n4. Nonprofit Organizations:\nLa Quadrature du Net: French advocacy group promoting digital rights and freedoms.\nTransparency France: Chapter of Transparency International, focusing on transparency, integrity, and accountability in governance.\n5. Academic Institutions:\nSorbonne University: One of the leading universities in France, offering research opportunities in various disciplines including computer science and cryptography.\nTélécom Paris: French engineering school focusing on information and communication technologies, offering research opportunities in cybersecurity.\n6. Crowdfunding:\nUlule: French crowdfunding platform supporting various creative and innovative projects.\nKissKissBankBank: French crowdfunding platform known for supporting projects in art, culture, and technology.\n7. Government Contracts:\nDirection Générale des Entreprises (DGE): French government agency responsible for implementing industrial policy, including cybersecurity initiatives.\nAgence Nationale de la Sécurité des Systèmes d'Information (ANSSI): French national cybersecurity agency overseeing the security of information systems, including potential collaborations on cryptosecure voting systems.\nWhen approaching these options, ensure your proposals are tailored to the specific interests and requirements of each entity, emphasizing the relevance of your research to their objectives."
                },
                {
                    "role": "user",
                    "content": "now for each points focus in " + place
                },
                ]
                response = generate(prompt, **chat_kwargs)
                print(response)
                list_places.append(place)
                preciseFundMe(list_places)
    else:
        print("too many requests, going back to menu")

OPENAI_API_KEY = "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"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

runing = True
while runing:
    request_limit = 0
    precisions = ""
    users_input = input(" 1:Inform me\n 2:Inspire me\n 3:Fund me\n 4:Leave\n> ")    
    if users_input=="1":
        informMe()
    elif users_input=="2":
        inspireMe()
    elif users_input=="3":
        fundMe()
    elif users_input=="4":
        runing=False

'''
i am developing a system for autonomous vehicles that is able to detect what is surrounding him and to take a decision depending on what was detected
'''
'''
    I am working on a thesis about a cryptosecure voting system.
'''