def emailTemplate(name: str, otp: str) -> str:
   html_template = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html>
    
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title></title>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Rubik">
        <style type="text/css">
            @media screen {{
                @font-face {{
                    font-family: 'Rubik';
                    font-style: normal;
                    font-weight: 400;
                    src: url(https://fonts.gstatic.com/s/rubik/v11/iJWZBXyIfDnIV5PNhY1KTN7Z-Yh-B4iFV0Uz.woff) format('woff');
                }}
            }}
    
            /* A simple css reset */
            @media only screen and (max-width: 620px) {{
                .wrapper .section {{
                    width: 100%;
                }}
    
                .wrapper .column {{
                    width: 100%;
                    display: block;
                }}
            }}
        </style>
    </head>
    
    <body
        style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
        <p
            style="margin:0;padding:0;padding-bottom:20px;line-height:1.6;font-family:'Rubik';color:#2d4f43;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;" />
        </p>
        <table width="100%"
            style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
            <tbody
                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                <tr
                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                    <td class="wrapper" width="600" align="center"
                        style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;padding-left:10px;padding-right:10px;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                        <table class="section header" cellpadding="0" cellspacing="0" width="600"
                            style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:initial;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                            <tr
                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                <td class="column"
                                    style="padding:0;margin:0;border: 1px solid #c3cdc9;border-radius:8px;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                    <table
                                        style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                        <tbody
                                            style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                            <tr
                                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                <td align="center"
                                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;padding-top: 64px;">
                                                    <h2
                                                        style="margin:0;padding:0;padding-bottom:20px;line-height:1.6;font-family:'Rubik';color:#2d4f43;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;text-align: center; padding-top: 32px; padding-bottom: 3px;">
                                                        Verificação de conta</h2>
                                                    <table
                                                        style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;margin-bottom: 48px;">
                                                        <tbody
                                                            style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                            <tr
                                                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                                <td
                                                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                                    <p style="margin:0;padding:0;padding-bottom:20px;line-height:1.6;font-family:'Rubik';color:#2d4f43;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
                                        display: inline-block;
                                        border-radius: 50%;
                                        width: 18px;
                                        height: 18px;
                                        padding: 8px;
                                        background: #c3cdc9;
                                        font-size: 16px;
                                        text-align: center;
                                        line-height: 17px;">O</p>
                                                                </td>
                                                                <td
                                                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;vertical-align: middle;">
                                                                    <p
                                                                        style="margin:0;padding:0;padding-bottom:20px;line-height:1.6;font-family:'Rubik';color:#2d4f43;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;padding: 0;">
                                                                        &nbsp;&nbsp;Urban Streewear</p>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr
                                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                <td align="left" style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;border-top: 1px solid #c3cdc9; 
                              padding: 46px 54px 64px;">
                                                    <p
                                                        style="margin:0;padding:0;padding-bottom:20px;line-height:1.6;font-family:'Rubik';color:#2d4f43;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; font-weight: 600;text-align: left;">
                                                        Olá, {username}!
                                                    </p>
                                                    <p
                                                        style="margin:0;padding:0;padding-bottom:20px;line-height:1.6;font-family:'Rubik';color:#2d4f43;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;text-align: left;">
                                                        Resgate o código abaixo para completar o seu cadastro
                                                    </p>
                                                    <p
                                                        style="margin:0;padding:0;padding-bottom:20px;line-height:1.6;font-family:'Rubik';color:#2d4f43;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;font-weight: 600;font-size:24px;text-align: center;">
                                                        {otp_code}
                                                    </p>
                                                    <p
                                                        style="margin:0;padding:0;padding-bottom:20px;line-height:1.6;font-family:'Rubik';color:#2d4f43;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;text-align: left;">
                                                        Seu código só é válido por cinco (5) minutos. Por favor, não compartilhe
                                                        com ninguém.
                                                    </p>
                                                    <p
                                                        style="margin:0;padding:0;padding-bottom:20px;line-height:1.6;font-family:'Rubik';color:#2d4f43;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;text-align: left;">
                                                        Se você não iniciou este login, entre em contato conosco.
                                                        <br>
                                                    </p>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            <tr
                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                <td class="column"
                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                    <table
                                        style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;width: 100%; border-bottom: 1px solid #c3cdc9;">
                                        <tbody
                                            style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                            <tr
                                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                <td align="center"
                                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            <tr
                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                <td class="column"
                                    style="padding: 0 135px;;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                    <table
                                        style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;width: 100%; margin-top: 32px; margin-bottom: 14px;"
                                        align="center">
                                        <tbody
                                            style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                            <tr
                                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                <td width="40%"
                                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                </td>
                                                <td width="20%"
                                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;vertical-align: middle;">
                                                </td>
                                                <td width="20%"
                                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;vertical-align: middle;">
                                                    <a href="https://www.linkedin.com/company/sprouthrtech/mycompany/"
                                                        target="_blank"><img src="https://via.placeholder.com/24x24"
                                                            style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;width:100%;display:block;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;width: 24px; margin:auto;" /></a>
                                                </td>
                                                <td width="40%"
                                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;vertical-align: middle;">
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            <tr
                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                <td class="column"
                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                    <table
                                        style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;width: 100%;">
                                        <tbody
                                            style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                            <tr
                                                style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;">
                                                <td
                                                    style="padding:0;margin:0;border:none;border-spacing:0px;border-collapse:collapse;vertical-align:top;font-family:'Rubik', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;text-align: center; font-size: 14px;">
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </body>
    
    </html>
    """
   
   return html_template.format(username=name, otp_code=otp)