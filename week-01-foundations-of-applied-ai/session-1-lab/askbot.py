"""
AskBot — Session 1 Lab starter
Practical AI for Software Engineering · Week 1

Work through the PARTs in order. Each has TODOs. Run the file after every part:
    python askbot.py

You only need to edit the sections marked TODO. Helper wiring is done for you.
"""

import os
import sys
import time
import argparse
from dotenv import load_dotenv
from openai import OpenAI

# --- provider wiring (done for you) ----------------------------------------
load_dotenv()
client = OpenAI(
    api_key=os.environ.get("LLM_API_KEY"),
    base_url=os.environ.get("LLM_BASE_URL"),
)
MODEL = os.environ.get("LLM_MODEL", "llama-3.3-70b-versatile")


# ===========================================================================
# PART 1 — Your first completion
#   Goal: send one prompt, print the reply.
# ===========================================================================
def ask_once(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


# ===========================================================================
# PART 2 — Interactive REPL with memory
#   Goal: a loop that keeps the conversation so the bot remembers context.
# ===========================================================================
def chat_loop(system_prompt: str, temperature: float):
    # TODO(2a): start `history` as a list containing ONE system message.
    history = [{"role": "system", "content": system_prompt}]
    
    # TODO(2b): loop forever:
    while True:
        #   - read input from the user with input("you > ")
        try:
            user_input = input("you > ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
            
        #   - if it's "quit" or "exit", break
        if user_input.lower().strip() in ["quit", "exit"]:
            break
            
        #   - append the user message to history
        history.append({"role": "user", "content": user_input})
        
        #   - call the API with the FULL history + temperature
        response = client.chat.completions.create(
            model=MODEL,
            messages=history,
            temperature=temperature
        )
        
        reply = response.choices[0].message.content
        
        #   - print the reply, and append the assistant message to history
        print(f"bot > {reply}")
        history.append({"role": "assistant", "content": reply})


# ===========================================================================
# PART 3 — CLI flags (done for you — wire your functions in)
# ===========================================================================
def main():
    parser = argparse.ArgumentParser(description="AskBot — a tiny LLM CLI")
    parser.add_argument("--persona", default="You are a concise, helpful assistant.",
                        help="System prompt / persona")
    parser.add_argument("--temp", type=float, default=0.7,
                        help="Temperature 0.0–2.0")
    parser.add_argument("--once", metavar="PROMPT",
                        help="Ask a single question and exit")
    args = parser.parse_args()

    if args.once:
        print(ask_once(args.once))
    else:
        print(f"AskBot ready (model={MODEL}, temp={args.temp}). Type 'quit' to exit.")
        chat_loop(args.persona, args.temp)


if __name__ == "__main__":
    main()
