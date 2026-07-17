#!/bin/bash

dirs=("accounts" "transactions" "budgets" "reports" "settings")

for dir in "${dirs[@]}"; do
    mkdir -p "app/templates/$dir"

    cat > "app/templates/$dir/index.html" <<EOF
{% extends "base.html" %}

{% block title %}
${dir^}
{% endblock %}

{% block content %}

<div class="container py-4">

    <h2>${dir^}</h2>

    <div class="alert alert-info">
        هذه الصفحة قيد التطوير.
    </div>

</div>

{% endblock %}
EOF

    echo "✅ app/templates/$dir/index.html"
done

echo "🎉 تم إنشاء جميع الصفحات."
