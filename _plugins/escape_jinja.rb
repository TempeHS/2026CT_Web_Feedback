Jekyll::Hooks.register :documents, :pre_render do |document|
  # Only process feedback.md files
  if document.path.end_with?('feedback.md')
    # Escape Jinja2 template syntax that conflicts with Liquid
    content = document.content
    
    # Escape all {% ... %} tags by wrapping them in backticks for inline code
    content = content.gsub(/\{\%[^%]*\%\}/) { |match| "`#{match}`" }
    
    # Escape all {{ ... }} variable syntax by wrapping in backticks
    content = content.gsub(/\{\{[^}]*\}\}/) { |match| "`#{match}`" }
    
    document.content = content
  end
end
