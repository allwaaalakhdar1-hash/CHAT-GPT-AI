# CHAT-GPT-AI

This project exposes two capabilities through a Flask application:

1. **Delivery Route Planner UI** – available at `/`, this page uses the Google Maps JavaScript
   API to let delivery representatives place multiple markers, automatically build an optimized
   driving route, and clear the plan when needed.
2. **Conversational product assistant** – available at `/chat`, this endpoint relays product
   questions to OpenAI's Chat Completions API and can enrich answers with matches from a
   WooCommerce catalog.

## Getting started

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables (or edit `app.py`) for:
   - `OPENAI_API_KEY`
   - WooCommerce credentials (`consumer_key`, `consumer_secret`, and `woocommerce_url`)
   - `GOOGLE_MAPS_API_KEY` (used by the map template)

3. Run the application:

   ```bash
   python app.py
   ```

4. Visit `http://localhost:10000/` to open the delivery route planner.

### 🇸🇦 إرشادات سريعة بالعربية

1. ثبّت المتطلبات عبر الأمر:

   ```bash
   pip install -r requirements.txt
   ```

2. أضف المتغيرات البيئية قبل تشغيل التطبيق:
   - مفتاح واجهة برمجة تطبيقات OpenAI في `OPENAI_API_KEY`
   - بيانات WooCommerce في `WOOCOMMERCE_CONSUMER_KEY` و`WOOCOMMERCE_CONSUMER_SECRET` و`WOOCOMMERCE_URL`
   - مفتاح خرائط Google في `GOOGLE_MAPS_API_KEY`

   على أنظمة يونكس يمكن ضبطها مؤقتًا كالتالي:

   ```bash
   export OPENAI_API_KEY="YOUR_KEY"
   export GOOGLE_MAPS_API_KEY="YOUR_GOOGLE_KEY"
   ```

3. شغّل التطبيق:

   ```bash
   python app.py
   ```

4. افتح المتصفح على `http://localhost:10000/` لمشاهدة الخريطة والتعامل معها.

## Using the route planner

- Click anywhere on the map to add stops in order.
- After two or more markers are placed, the map automatically draws the driving route.
- Intermediate stops are optimized using the Google Directions Service while keeping the first
  and last points fixed as origin and destination.
- Use the **Clear markers & route** button to reset the plan.
