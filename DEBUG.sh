echo "= Setting local environment"

export DEBUG=true
export DATABASE_URL="sqlite:///./dicy-story.db"

echo "= DEBUG: $DEBUG"
echo "= DATABASE_URL: $DATABASE_URL"
