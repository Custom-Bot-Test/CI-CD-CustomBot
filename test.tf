

resource "cloudflare_record" "testing" {
  zone_id    = var.zone_id
  name       = "testing"
  value      = aws_eip.eip.public_dns
  type       = "CNAME"
  ttl        = 1
  proxied    = true
  depends_on = [aws_instance.public]
}