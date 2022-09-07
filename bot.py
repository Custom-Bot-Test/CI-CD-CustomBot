import typer
import subprocess



bot = typer.Typer()


@bot.command("commit-sub")
def commit_subdomain(subdomain: str = 'cloud', message: str = 'ran commit-sub', branch: str = 'main'):

    template = """
resource "cloudflare_record" "%s" {
  zone_id    = var.zone_id
  name       = "%s"
  value      = aws_eip.eip.public_dns
  type       = "CNAME"
  ttl        = 1
  proxied    = true
  depends_on = [aws_instance.public]
}"""
    with open("test.tf", 'a') as cloudflare_tf:
        cloudflare_tf.write(template % (subdomain, subdomain))
    
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-am", message])
    subprocess.call(["git", "push", "origin", branch])


@bot.command("commit")
def test():
    print("Test ran successfully.")

    
if __name__=="__main__":
    bot()
