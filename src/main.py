# Build Gradio interface
with gr.Blocks(css="footer {visibility: hidden}") as demo:
    gr.Markdown("## 🎨 AI Text-to-Image Generator - SDXL Edition")

    with gr.Tab("🖼️ Generate Image"):
        with gr.Row():
            with gr.Column(scale=2):
                prompt = gr.Textbox(label="Prompt", placeholder="e.g., A wizard standing on a cliff...")
                enhance_btn = gr.Button("✨ Enhance Prompt")
                style = gr.Dropdown(["Realistic", "Anime", "Cyberpunk", "Sketch", "Oil Painting"], label="Style", value="Realistic")
                aspect = gr.Radio(["1:1", "16:9", "9:16"], label="Aspect Ratio", value="1:1")
                neg_prompt = gr.Textbox(label="Negative Prompt (optional)", placeholder="e.g., blurry, distorted, low quality")
                generate_btn = gr.Button("Generate 🔥")

            with gr.Column(scale=3):
                output_img = gr.Image(label="Generated Image", type="pil")
                download_btn = gr.Button("📥 Download Image")
                history_gallery = gr.Gallery(label="🕓 Generation History", show_label=True, columns=3)

    # with gr.Tab("📋 Login"):
    #     username = gr.Textbox(label="Username")
    #     password = gr.Textbox(label="Password", type="password")
    #     login_btn = gr.Button("🔐 Login")
    #     welcome_text = gr.Textbox(label="Status", interactive=False)
    #     login_panel = gr.Group(visible=False)

    #     login_btn.click(fn=simulate_login, inputs=[username, password], outputs=[welcome_text, login_panel])

    # with login_panel:
    #     gr.Markdown("✅ You are now logged in. Start generating awesome images!")

    # Event bindings
    enhance_btn.click(fn=enhance_prompt, inputs=prompt, outputs=prompt)

    image_list = []

    def generate_and_save(prompt, style, aspect, neg_prompt):
        img = generate_image(prompt, style, aspect, neg_prompt)
        image_list.append(img)
        return img, image_list

    generate_btn.click(fn=generate_and_save, inputs=[prompt, style, aspect, neg_prompt], outputs=[output_img, history_gallery])

    # Allow download (for full functionality, you could create a file link if needed)
    def download_image(img):
        path = "generated_image.png"
        img.save(path)
        return path

    download_btn.click(fn=download_image, inputs=output_img, outputs=gr.File(label="Download Link"))

# Launch app
demo.launch()

