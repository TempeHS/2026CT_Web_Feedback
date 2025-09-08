Jekyll::Hooks.register :documents, :pre_render do |document|
  # Only process feedback.md files
  if document.path.end_with?('feedback.md')
    # Escape Jinja2 template syntax that conflicts with Liquid
    content = document.content
    
    # Escape {% extends %} tags
    content = content.gsub(/\{\%\s*extends\s+[^%]*\%\}/, '`\\0`')
    
    # Escape {% include %} tags  
    content = content.gsub(/\{\%\s*include\s+[^%]*\%\}/, '`\\0`')
    
    # Escape {% block %} tags
    content = content.gsub(/\{\%\s*block\s+[^%]*\%\}/, '`\\0`')
    content = content.gsub(/\{\%\s*endblock\s*\%\}/, '`\\0`')
    
    # Escape {% for %} tags
    content = content.gsub(/\{\%\s*for\s+[^%]*\%\}/, '`\\0`')
    content = content.gsub(/\{\%\s*endfor\s*\%\}/, '`\\0`')
    
    # Escape {% if %} tags
    content = content.gsub(/\{\%\s*if\s+[^%]*\%\}/, '`\\0`')
    content = content.gsub(/\{\%\s*endif\s*\%\}/, '`\\0`')
    
    # Escape {{ variable }} syntax
    content = content.gsub(/\{\{[^}]*\}\}/, '`\\0`')
    
    document.content = content
  end
end
