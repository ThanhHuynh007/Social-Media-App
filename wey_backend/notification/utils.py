from .models import Notification

from post.models import Post
from account.models import FriendshipRequest

# create_notification(request, 'post_like', 'lskjf-j12l3-jlas-jdfa', 'lskjf-j12l3-jlas-jdfa')


def create_notification(request, type_of_notification, post_id=None, friendrequest_id=None):
    created_for = None

    if type_of_notification == 'post_like':
        body = f'{request.user.name} đã thích một bài viết của bạn!'
        post = Post.objects.get(pk=post_id)
        created_for = post.created_by
    elif type_of_notification == 'post_comment':
        body = f'{request.user.name} đã bình luận trên một bài viết của bạn!'
        post = Post.objects.get(pk=post_id)
        created_for = post.created_by
    elif type_of_notification == 'new_friendrequest':
        friendrequest = FriendshipRequest.objects.get(pk=friendrequest_id)
        created_for = friendrequest.created_for
        body = f'{request.user.name} đã gửi cho bạn một lời mời kết bạn!'
    elif type_of_notification == 'accepted_friendrequest':
        friendrequest = FriendshipRequest.objects.get(pk=friendrequest_id)
        created_for = friendrequest.created_for
        body = f'{request.user.name} đã chấp nhận lời mời kết bạn của bạn!'
    elif type_of_notification == 'rejected_friendrequest':
        friendrequest = FriendshipRequest.objects.get(pk=friendrequest_id)
        created_for = friendrequest.created_for
        body = f'{request.user.name} đã từ chối lời mời kết bạn của bạn!'

    notification = Notification.objects.create(
        body=body,
        type_of_notification=type_of_notification,
        created_by=request.user,
        post_id=post_id,
        created_for=created_for
    )

    return notification
