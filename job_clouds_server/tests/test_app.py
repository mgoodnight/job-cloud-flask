def test_generate_image(client, gen_image_good):
    res = client.post('/generate', json=gen_image_good)
    assert res.status_code == 200


def test_invalid_channel(client, gen_image_invalid_channel):
    res = client.post('/generate', json=gen_image_invalid_channel)
    assert res.status_code == 400
    assert "Please provide a valid channel" in res.data.decode('utf-8')


def test_invalid_theme(client, gen_image_invalid_theme):
    res = client.post('/generate', json=gen_image_invalid_theme)
    assert res.status_code == 400
    assert "Please provide a valid theme" in res.data.decode('utf-8')
