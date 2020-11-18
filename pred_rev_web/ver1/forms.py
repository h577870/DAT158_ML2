from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SubmitForm(FlaskForm):
    channelGrouping              = StringField("channelGrouping", validators=[DataRequired(), Length(min=2,max=50)])
    fullVisitorId                = StringField("fullVisitorId", validators=[DataRequired(), Length(min=2,max=50)])
    socialEngagementType         = StringField("socialEngagementType", validators=[DataRequired(), Length(min=2,max=50)])
    visitId                      = StringField("visitId", validators=[DataRequired(), Length(min=2,max=50)])
    visitNumber                  = StringField("visitNumber", validators=[DataRequired(), Length(min=2,max=50)])
    device_browser               = StringField("device_browser", validators=[DataRequired(), Length(min=2,max=50)])
    device_operatingSystem       = StringField("device_operatingSystem", validators=[DataRequired(), Length(min=2,max=50)])
    device_isMobile              = StringField("device_isMobile", validators=[DataRequired(), Length(min=2,max=50)])
    device_deviceCategory        = StringField("device_deviceCategory", validators=[DataRequired(), Length(min=2,max=50)])
    geoNetwork_continent         = StringField("geoNetwork_continent", validators=[DataRequired(), Length(min=2,max=50)])
    geoNetwork_country           = StringField("geoNetwork_country", validators=[DataRequired(), Length(min=2,max=50)])
    totals_visits                = StringField("totals_visits", validators=[DataRequired(), Length(min=2,max=50)])
    totals_hits                  = StringField("totals_hits", validators=[DataRequired(), Length(min=2,max=50)])
    totals_pageviews             = StringField("totals_pageviews", validators=[DataRequired(), Length(min=2,max=50)])
    totals_bounces               = StringField("totals_bounces", validators=[DataRequired(), Length(min=2,max=50)])
    totals_newVisits             = StringField("totals_newVisits", validators=[DataRequired(), Length(min=2,max=50)])
    #totals_transactionRevenue    = StringField("totals_transactionRevenue ", validators=[DataRequired(), Length(min=2,max=50)])
    trafficSource_isTrueDirect   = StringField("trafficSource_isTrueDirect", validators=[DataRequired(), Length(min=2,max=50)])

    submit = SubmitField("Predict")